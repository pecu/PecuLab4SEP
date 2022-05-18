pragma solidity >=0.8.0 <0.9.0;
// SPDX-License-Identifier: MIT

import "@openzeppelin/contracts/access/Ownable.sol";
import './PecuCoin.sol';

contract Vendor is Ownable {

  PecuCoin2 yourToken;
  
  uint256 public tokensPerEth = 100;

  event BuyTokens(address buyer, uint256 amountOfEth, uint256 amountOfTokens);

  constructor() {
    yourToken = PecuCoin2(0x970fD02DF663A6379D65566EDa2383D953133d8f);
  }

  function buyTokens() payable public {
    require(msg.value > 0, "Not enought ether");

    uint256 amountOfTokens = msg.value * tokensPerEth;

    uint256 tokenBalance = yourToken.balanceOf(address(this));
    require(tokenBalance > amountOfTokens, "Not enought tokens");
    
    bool sent =  yourToken.transfer(msg.sender, amountOfTokens);
    require(sent, "Failed to transfer token to the buyer");

    emit BuyTokens(msg.sender, msg.value, amountOfTokens);
  }

  function withdraw() public onlyOwner {

    uint256 balance = address(this).balance;
    require(balance > 0, "No ether to withdraw");
    
    (bool sent, ) = msg.sender.call{value: balance}("");
    require(sent, "Failed to withdraw balance");
  }
}
