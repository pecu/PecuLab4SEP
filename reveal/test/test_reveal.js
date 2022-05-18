const { expect } = require("chai");

describe("NFT Reveal contract", function () {
    it("Deployment should assign the NFT Reveal contract to the minter", async function () {
      const NFT = await ethers.getContractFactory("NFT");
      
      const _name = "NFT Reveal";
      const _symbol = "NFT";
      const _initBaseURI = "https://raw.githubusercontent.com/pecu/PecuLab4SEP/main/NFT-ERC1155/";
      const _initNotRevealedUri = "https://raw.githubusercontent.com/pecu/PecuLab4SEP/main/NFT-ERC1155/0.json";
      
      const nft = await NFT.deploy(_name, _symbol, _initBaseURI, _initNotRevealedUri);

      await nft.deployed();

      const tokenuri1 = await nft.tokenURI(1);
      console.log(tokenuri1);

      await nft.reveal();
      const tokenuri2 = await nft.tokenURI(2);
      console.log(tokenuri2);

      const wallet = await nft.walletOfOwner("0xAbaA9D9c354163781718694260C7eD87538aA127");
      console.log(wallet);
    });
  });