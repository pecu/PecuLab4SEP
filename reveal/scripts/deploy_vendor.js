const hre = require("hardhat");

// You might need the previously deployed yourToken:
async function main() {

  const Vendor = await hre.ethers.getContractFactory("Vendor");
  const vendor = await Vendor.deploy();
  await vendor.deployed();

  console.log("vendor deployed to:", vendor.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});