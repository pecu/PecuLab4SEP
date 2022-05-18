// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableMap.sol";
import "./IMineMintRandom.sol";

contract MineNft is ERC721Enumerable, Pausable, AccessControl {

    // Minted event
    event Minted(address indexed player, uint256 tokenId);

    // Burned event
    event Burned(address indexed player, uint256 tokenId);

    // Rank Type
    enum RankType {
        GOLD,
        DIAMOND,
        EMERALD,
        OBISIDIAN,
        NETHERITE
    }

    /**
     * ON-CHAIN METADATA
     */

    struct Metadata {
        bool puritySet;
        uint16 purity; // goes from 0 to 10_000
        RankType rankType;
        uint256 created;
    }

    // mapping from token ID to its metadata
    mapping(uint256 => Metadata) public metadata;

    /**
     * ROLES
     */
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant FORGE_ROLE = keccak256("FORGE_ROLE");
    bytes32 public constant ORACLE_ROLE = keccak256("ORACLE_ROLE");
    bytes32 public constant VRF_ROLE = keccak256("VRF_ROLE");

    /**
     * STATS VARIABLES
     */
    // token ID counter
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    /**
     * ORCALE VARIABLES
     */
    // gold rank price
    uint256 public GOLD_RANK_PRICE = 200 * 10**18;

    /**
     * ADMIN VARIABLES
     */
    // address for the reward pool
    address public REWARD_POOL;
    // address for the dev fees
    address public DEV_FEES;
    // stop presale minting
    bool public presaleActive = true;
    // enable gold trading
    bool public goldTradingEnabled = false;
    // enable gold minting
    bool public goldMintingEnabled = true;

    /**
     * OTHER VARIABLES
     */
    // metadata url
    string private TOKEN_URI_PREFIX = "https://api.minecrypto.gg/rank/";
    // contract of the token used for minting
    IERC20 private TOKEN_CONTRACT; // todo test public
    // contract of the RNG
    IMineMintRandom private MINE_RANDOM; // todo test public

    constructor() ERC721("MineCrypto Rank", "MINER") {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);
        _setupRole(ORACLE_ROLE, msg.sender);
        _setupRole(FORGE_ROLE, msg.sender);
        _setupRole(VRF_ROLE, msg.sender);
    }

    function transferOwnership(address newOwner) external {
        grantRole(DEFAULT_ADMIN_ROLE, newOwner);
        renounceRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }

    /**
     * MINTING
     */

    /**
     * @dev allows minting NFTs by paying a fee
     */
    function mint() external whenNotPaused returns (uint256) {
        require(goldMintingEnabled, "Gold rank minting is paused");
        _requirePayment(GOLD_RANK_PRICE);
        return _mintRank(msg.sender, RankType.GOLD);
    }

    /**
     * @dev allows minting NFTs without paying fee
     */
    function mintUnclaimed(address player)
        external
        whenNotPaused
        onlyRole(MINTER_ROLE)
        returns (uint256)
    {
        return _mintRank(player, RankType.GOLD);
    }

    /**
     * @dev allows setting purity from VRF or minter
     */
    function setPurity(uint256 tokenId, uint256 randomness) external whenNotPaused {
        require(
            hasRole(FORGE_ROLE, msg.sender) || hasRole(VRF_ROLE, msg.sender),
            "Caller is not forge or vrf"
        );

        metadata[tokenId].purity = uint16(randomness % 10_001);
        metadata[tokenId].puritySet = true;
    }

    /**
     * @dev allows minting NFTs on the presale
     */
    function mintPresale(RankType rankType, address player)
        external
        whenNotPaused
        onlyRole(MINTER_ROLE)
        returns (uint256)
    {
        require(presaleActive, "Presale has ended");
        return _mintRank(player, rankType);
    }

    /**
     * @dev actually mints a rank and sets its metadata
     * @param player reciever of the rank
     * @param rankType the type of the new rank
     */
    function _mintRank(address player, RankType rankType) private returns (uint256) {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(player, newItemId);
        metadata[newItemId].rankType = rankType;
        metadata[newItemId].created = block.timestamp;

        MINE_RANDOM.getRandomMintPurity(newItemId);

        emit Minted(player, newItemId);

        return newItemId;
    }

    /**
     * @dev burns a rank given its id, can only be done by forge or owner
     * @param tokenId nft being burned
     */
    function burn(uint256 tokenId) external whenNotPaused {
        require(
            // msg.sender == ownerOf(tokenId) || hasRole(FORGE_ROLE, msg.sender),
            _isApprovedOrOwner(msg.sender, tokenId),
            "Only owner or forge can burn"
        );

        emit Burned(msg.sender, tokenId);

        _burn(tokenId);
    }

    /**
     * FUNCTIONS TO BE CALLED FROM THE FORGE
     */

    /**
     * @dev allows minting NFTs on the forge
     */
    function mintRankForge(address player, RankType rankType)
        external
        onlyRole(FORGE_ROLE)
        whenNotPaused
        returns (uint256)
    {
        return _mintRank(player, rankType);
    }

    /**
     * ADMINISTRATION FUNCTIONS
     */

    /**
     * @dev stops the presale forever
     */
    function endPresale() external onlyRole(DEFAULT_ADMIN_ROLE) {
        presaleActive = false;
    }

    /**
     * @dev allows changing the uri prefix
     */
    function setTokenUri(string calldata newPrefix) external onlyRole(DEFAULT_ADMIN_ROLE) {
        TOKEN_URI_PREFIX = newPrefix;
    }

    /**
     * @dev controls the gold rank trading
     * @param enabled new state
     */
    function setGoldTradingEnabled(bool enabled) external onlyRole(DEFAULT_ADMIN_ROLE) {
        goldTradingEnabled = enabled;
    }

    /**
     * @dev controls the gold rank minting
     * @param enabled new state
     */
    function setGoldMintingEnabled(bool enabled) external onlyRole(DEFAULT_ADMIN_ROLE) {
        goldMintingEnabled = enabled;
    }

    /**
     * @dev sets the token used for fees
     * @param newAddress new token address
     */
    function setTokenAddress(address newAddress) external onlyRole(DEFAULT_ADMIN_ROLE) {
        TOKEN_CONTRACT = IERC20(newAddress);
    }

    /**
     * @dev sets the vrf address
     * @param newAddress new vrf address
     */
    function setVrfAddress(address newAddress) external onlyRole(DEFAULT_ADMIN_ROLE) {
        MINE_RANDOM = IMineMintRandom(newAddress);
    }

    /**
     * @dev sets the address of the reward pool
     * @param newAddress new token address
     */
    function setRewardPoolAddress(address newAddress) external onlyRole(DEFAULT_ADMIN_ROLE) {
        REWARD_POOL = newAddress;
    }

    /**
     * @dev sets the address of the dev fees address
     * @param newAddress new token address
     */
    function setDevFeesAddress(address newAddress) external onlyRole(DEFAULT_ADMIN_ROLE) {
        DEV_FEES = newAddress;
    }

    /**
     * @dev allows withdrawing any token that is stuck in the contract
     * @param tokenAddress addres of the token we are withdrawing
     */
    function emergencyWithdrawToken(address tokenAddress) external onlyRole(DEFAULT_ADMIN_ROLE) {
        IERC20 tokenContract = IERC20(tokenAddress);

        uint256 withdrawBalance = tokenContract.balanceOf(address(this));

        require(withdrawBalance > 0, "No balance for this token");

        tokenContract.transfer(msg.sender, withdrawBalance);
    }

    /**
     * @dev allows withdrawing BNB that is stuck in the contract
     */
    function emergencyWithdrawBNB() external onlyRole(DEFAULT_ADMIN_ROLE) {
        payable(msg.sender).transfer(address(this).balance);
    }

    /**
     * ORACLE FUNCTIONS
     */

    /**
     * Sets the new gold rank mint cost
     * @param amount amount of tokens
     */
    function setMintCost(uint256 amount) external onlyRole(ORACLE_ROLE) {
        GOLD_RANK_PRICE = amount;
    }

    /**
     * PAUSABLE FUNCTIONS
     */

    /**
     * @dev pauses the contract
     */
    function pause() external onlyRole(DEFAULT_ADMIN_ROLE) {
        _pause();
    }

    /**
     * @dev unpauses the contract
     */
    function unpause() external onlyRole(DEFAULT_ADMIN_ROLE) {
        _unpause();
    }

    /**
     * @dev Allow disabling gold ranks transfer (if they are not burns or mints) and pausing
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override whenNotPaused {
        require(
            goldTradingEnabled ||
                from == address(0) ||
                to == address(0) ||
                metadata[tokenId].rankType != RankType.GOLD,
            "You can't trade gold ranks"
        );

        super._beforeTokenTransfer(from, to, tokenId);
    }

    /**
     * METADATA FUNCTIONS
     */

    /**
     * @dev returns the base uri for the metadata
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return TOKEN_URI_PREFIX;
    }

    /**
     * @dev returns the purity of an nft
     */
    function getPurity(uint256 tokenId) external view returns (uint16) {
        require(metadata[tokenId].puritySet, "Purity not set yet");
        return metadata[tokenId].purity;
    }

    /**
     * @dev returns the type of an nft
     */
    function getType(uint256 tokenId) external view returns (RankType) {
        return metadata[tokenId].rankType;
    }

    /**
     * @dev returns the time an nft was created
     */
    function getCreated(uint256 tokenId) external view returns (uint256) {
        return metadata[tokenId].created;
    }

    /**
     * STATS FUNCTIONS
     */

    /**
     * @dev returns the current max token id
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIds.current();
    }

    /**
     * PAYMENTS FUNCTION
     */

    /**
     * @dev creates a token payment and splits the fees
     * @param amount tokens to be spent
     */
    function _requirePayment(uint256 amount) private {
        if (amount == 0) return;

        require(
            TOKEN_CONTRACT.allowance(msg.sender, address(this)) > amount,
            "Not enough allowance"
        );

        require(
            TOKEN_CONTRACT.transferFrom(msg.sender, address(this), amount),
            "Error transfering tokens"
        );

        TOKEN_CONTRACT.transfer(REWARD_POOL, amount / 2);
        TOKEN_CONTRACT.transfer(DEV_FEES, amount / 2);
    }

    /**
     * MISC
     */

    function supportsInterface(bytes4 interfaceId)
        public
        view
        virtual
        override(ERC721Enumerable, AccessControl)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}