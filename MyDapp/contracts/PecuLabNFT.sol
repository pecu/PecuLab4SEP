// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PecuLab is ERC721, Ownable {
    constructor() ERC721("PecuLab", "PID") {}

    function _baseURI() internal pure override returns (string memory) {
        return "https://ipfs.io/ipfs/QmTYGpSLy511SKNH34uE1WNbo4ixB2FTa6t7qr82rDH5VQ?filename=PID0003";
    }

    function safeMint(address to, uint256 tokenId) public onlyOwner {
        _safeMint(to, tokenId);
    }
}