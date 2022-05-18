const hre = require("hardhat");

// You might need the previously deployed yourToken:
async function main() {

  const MineNft = await hre.ethers.getContractFactory("MineNft");
  const mineNft = await MineNft.deploy();
  await mineNft.deployed();

  console.log("mineNft deployed to:", mineNft.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});