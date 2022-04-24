const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("PecuLab", function () {
  it("Should return the new PecuLab once it's changed", async function () {
    const PecuLab = await hre.ethers.getContractFactory("PecuLab");
    const pecuLab = await PecuLab.deploy();
  
    await pecuLab.deployed();

  });
});
