const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("PecuCoin", function () {
  it("Should return the new PecuCoin once it's changed", async function () {
    const PecuCoin = await hre.ethers.getContractFactory("PecuCoin");
    const pecucoin = await PecuCoin.deploy();
  
    await pecucoin.deployed();

  });
});
