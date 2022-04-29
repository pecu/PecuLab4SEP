// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "hardhat/console.sol";

contract PuzzleNFT is ERC1155, Ownable  {

    mapping (uint256 => string) private _tokenURIs;
    using Strings for uint256;
    string private _blindTokenURI = "https://raw.githubusercontent.com/pecu/PecuLab4SEP/main/NFT-ERC1155/PID0000.json";
    string private _baseURI = "https://raw.githubusercontent.com/pecu/PecuLab4SEP/main/NFT-ERC1155/PID000";
    string private _text = "";

    constructor() ERC1155("") {
        _setURI(_blindTokenURI);
    }

    function setBlindBoxOpened(uint256 id) public {
        _text = string(abi.encodePacked(_baseURI, Strings.toString(id)));
        _setURI(string(abi.encodePacked(_text, ".json")));
        console.log("Opened URI %s id %d", uri(id), id);
    }

    function setBlindBoxClosed(uint256 id) public {
        _setURI(_blindTokenURI);            
        console.log("Closed URI %s id %d", uri(id), id);
    }

    function mint(address account, uint256 id) public onlyOwner {
        _mint(account, id, 1, "");
    }     
}
