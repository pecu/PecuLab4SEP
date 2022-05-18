// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract PecuCoin2 is ERC20 {
    constructor() ERC20("PecuCoin2", "PCO") {
        _mint(msg.sender, 200000000 * 10 ** decimals());
    }
}