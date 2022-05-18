// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// When running the script with `npx hardhat run <script>` you'll find the Hardhat
// Runtime Environment's members available in the global scope.
const hre = require("hardhat");

async function main() {
  // Hardhat always runs the compile task when running scripts with its command
  // line interface.
  //
  // If this script is run directly using `node` you may want to call compile
  // manually to make sure everything is compiled
  // await hre.run('compile');

  // We get the contract to deploy
  const NFT = await ethers.getContractFactory("NFT");

  const _name = "NFT Reveal";
  const _symbol = "NFT";
  const _initBaseURI = "https://raw.githubusercontent.com/pecu/PecuLab4SEP/main/NFT-ERC1155/";
  const _initNotRevealedUri = "https://raw.githubusercontent.com/pecu/PecuLab4SEP/main/NFT-ERC1155/0.json";
  
  const nft = await NFT.deploy(_name, _symbol, _initBaseURI, _initNotRevealedUri);

  await nft.deployed();

  console.log("nft deployed to:", nft.address);
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
