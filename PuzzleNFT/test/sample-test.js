const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("PuzzleNFT", function () {
  it("Should return the new puzzle once it's changed", async function () {
    const PuzzleNFT = await ethers.getContractFactory("PuzzleNFT");
    const puzzle = await PuzzleNFT.deploy();
    await puzzle.deployed();

    const setBlindBoxOpened1 = await puzzle.setBlindBoxOpened(5);
    const mint = await puzzle.mint("0xAbaA9D9c354163781718694260C7eD87538aA127", 5);
    const setBlindBoxClosed1 = await puzzle.setBlindBoxClosed(5);
    const setBlindBoxOpened2 = await puzzle.setBlindBoxOpened(5);
    const setBlindBoxClosed2 = await puzzle.setBlindBoxClosed(5);

  });
});
