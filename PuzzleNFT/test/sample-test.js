const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("PuzzleNFT", function () {
  it("Should return the new puzzle once it's changed", async function () {
    const PuzzleNFT = await ethers.getContractFactory("PuzzleNFT");
    const puzzle = await PuzzleNFT.deploy();
    await puzzle.deployed();

    await puzzle.tokenURI(5);
    await puzzle.flipReveal();
    await puzzle.tokenURI(5);
    const geturi = await puzzle.uri(5);
    console.log(geturi);
  });
});
