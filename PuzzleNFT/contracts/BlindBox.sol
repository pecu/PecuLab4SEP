// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "hardhat/console.sol";

contract PuzzleNFT is ERC1155, Ownable  {

    using Strings for uint256;

    bool public _revealed = false;  //init in blind box
    uint256 public mintPrice = 0.03 ether;

    string public baseURI;
    string public baseExtension = ".json";

    mapping(uint256 => string) private _tokenURIs;

    string private initNotRevealedUri = "ipfs://Qma8vNBBEFxY7LHcpNNWhxzV2DRnwf1xbk4ARxxgYHGKtX";
    string private initBaseURI = "ipfs://QmbbCkbmZTbqopwsYDS6G2pvC4W2UeQZYZruwnNzaXyF38/";

    constructor() ERC1155(initNotRevealedUri)
    {
        setBaseURI(initBaseURI);
        mint(msg.sender, 5);
    }

    function setBaseURI(string memory _newBaseURI) public onlyOwner {
        baseURI = _newBaseURI;
    }

    function mint(address account, uint256 id) public onlyOwner {
        _mint(account, id, 10, "");
    }

    function tokenURI(uint256 tokenId)
        public
        virtual
        returns (string memory)
    {
        if (_revealed == false) {
            console.log(initNotRevealedUri);
            return initNotRevealedUri;
        }

        string memory _tokenURI = _tokenURIs[tokenId];
        string memory base = _baseURI();
        string memory tempURI = "";

        // If there is no base URI, return the token URI.
        if (bytes(base).length == 0) {
            _setURI(tempURI);
            console.log(_tokenURI);
            return _tokenURI;
        }
        // If both are set, concatenate the baseURI and tokenURI (via abi.encodePacked).
        if (bytes(_tokenURI).length > 0) {
            tempURI = string(abi.encodePacked(base, _tokenURI));
            _setURI(tempURI);
            console.log(tempURI);
            return tempURI;
        }
        // If there is a baseURI but no tokenURI, concatenate the tokenID to the baseURI.
        tempURI = string(abi.encodePacked(base, tokenId.toString(), baseExtension));
        _setURI(tempURI);
        console.log(tempURI);
        return tempURI;
    }

    // internal
    function _baseURI() internal view virtual returns (string memory) {
        return baseURI;
    }

    // open blind box
    function flipReveal() public onlyOwner {
        if( _revealed == false )
        {
            _revealed = !_revealed;
        }        
    }

    function setMintPrice(uint256 _mintPrice) public onlyOwner {
        mintPrice = _mintPrice;
    }

    function setBaseExtension(string memory _newBaseExtension)
        public
        onlyOwner
    {
        baseExtension = _newBaseExtension;
    }
    
    function withdraw(address to) public onlyOwner {
        uint256 balance = address(this).balance;
        payable(to).transfer(balance);
    }
}