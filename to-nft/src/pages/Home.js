import { useWeb3React } from "@web3-react/core";
import { InjectedConnector } from "@web3-react/injected-connector";
import Web3 from 'web3';
import React, { useState } from "react";
import abi from "../ABI/peculab.json";
import { Button } from "@mui/material";
import * as IPFS from 'ipfs-core';

const Home = () => {
  const [balance, setBalance] = useState(0);
  const [NFTuri, setNFT] = useState(0);
  const [toWeb3Text, toWeb3NFT] = useState(0);

  const key = 'y6ubyFhm0QrMuOQz4qYLZQKNjJ9a3uNz';
  //const key = 'rgoyf-iXewqRwAnf5cGe3uEz6jCMzz2n';
  const host = 'https://eth-goerli.g.alchemy.com/v2/' + key;  
  
  // Making injected setup ready here
  const injected = new InjectedConnector({
    supportedChainIds: [
      1, // Mainet
      5, // Goerli
      10001, // ETHW-mainnet
    ],
  });

  // Getting all the functions of useWeb3React library
  const { account, activate, library } = useWeb3React();

  // Fn to enable wallet
  const connectWallet = async () => {
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    await activate(injected);

    const cookies = document.cookie.split(';').map(cookie => cookie.trim().split('='));
    const myCookie = cookies.find(cookie => cookie[0] === 'myCookie');
    console.log(`The cookie is ${myCookie[1]}`);
    var toText = myCookie[1];
    toWeb3NFT(toText);
  };

  const getUserNFT = async () => {
    const provider = new Web3.providers.HttpProvider(host);
    const web3 = new Web3(provider);
    const contract = new web3.eth.Contract(abi, "0xf4910C763eD4e47A585E2D34baA9A4b611aE448C");
    const tokenId  = '77646948894287454690056914056512259301233960084258847748628249723401863692338';

    console.log("abi:" + abi);    
    contract.methods.uri(tokenId).call().then(uri => {

      const ipfsUrl = uri;
      const ipfsGateway = "https://ipfs.io/ipfs/";
      const httpsUrl = ipfsUrl.replace("ipfs://", ipfsGateway + "");

      setNFT(httpsUrl);
    })        
  };

  const WriteUserNFT = async () => {
    const attributeNameID = 2;
    const attributeValue = toWeb3Text;
    
    const controller = new AbortController();
    const signal = controller.signal;
    fetch(NFTuri, {signal}).then(response => response.json()).then(metadata => {
      console.log(metadata.properties[attributeNameID].value);
      metadata.properties[attributeNameID].value = attributeValue;
      console.log(metadata.properties[attributeNameID].value);
      console.log("mint a new cid");
      ipfsGO(metadata);

    }).catch(error => console.error(error)).finally(() => {
      // 不論請求成功還是失敗，都取消 timeout 計時器
      controller.abort();
    });
  };

  const ipfsGO = async (metadata) => {   

    const jsonString = JSON.stringify(metadata);
    const file = new Blob([jsonString], { type: 'text/plain' });
    const reader = new FileReader();

    reader.onload = async () => {
      const ipfs = await IPFS.create();
      const buffer = new Uint8Array(reader.result);
      const options = {
        cidVersion: 1
      };
      const result = await ipfs.add(buffer, options);
      console.log(result.cid.toString());

      const cid = result.cid.toString();
      const data = await ipfs.cat(cid);
      console.log(data.toString());

      const uri = 'ipfs://' + cid;
      console.log(uri);

      mint(uri);

    };
    reader.readAsArrayBuffer(file);        
      
    const mint = async (uri) => {
      const provider = new Web3.providers.HttpProvider(host);
      const web3 = new Web3(provider);
      const contractAddress = "0xf4910C763eD4e47A585E2D34baA9A4b611aE448C";
      const contract = new web3.eth.Contract(abi, contractAddress);
      
      console.log("account:" + account);

      const gasPrice = await contract.methods.mint(account, 1, 1, 0x00).estimateGas();
      const nonce = await web3.eth.getTransactionCount(account);
      const txData = contract.methods.mint(account, 0, 1, 0x00).encodeABI();
      const txParams = {
        from: account,
        to: contractAddress,
        data: txData,
        gas: gasPrice.toString(),
        nonce: nonce.toString(),
        gasLimit: web3.utils.toHex(300000) // 可自行調整
      };
      
      try {
        const txHash = await window.ethereum.request({
          method: 'eth_sendTransaction',
          params: [txParams]
        });
        console.log('Transaction sent:', txHash);      
        // 監聽交易回應
        provider.on('transactionHash', (txHash) => {
          console.log('Transaction pending:', txHash);
        });      
        provider.on('confirmation', (confirmationNumber, receipt) => {
          console.log('Transaction confirmed:', receipt);
        });      
        provider.on('error', (err) => {
          console.error('Transaction error:', err);
        });
      } catch (error) {
        console.error('Transaction failed:', error);
      }
      /*
       const Tx = await window.ethereum.request({
        method: 'eth_sendTransaction',
        params: [{
          from: account,
          to: contractAddress,
          data: contract.methods.setURI(tokenId, uri).encodeABI(),
          gas: gasPrice
        }]
      });
      this.setState({ txBeingSent: Tx.hash });
      */      
    };
  };

  // Fn to get user native token balance
  const getUserBalance = async () => {
    library?.getBalance(account).then((result) => {
      setBalance(result / 1e18);
    });
  };
 
  return (
    <div align="left">
      Wallet Address:{" "}<strong style={{ fontSize: 13, color: "black" }}>{account}</strong>{" "}
      to NFT Data:{" "}<strong style={{ fontSize: 13, color: "black" }}>{toWeb3Text}</strong>{" "}
      <div>
      <Button onClick={getUserBalance}>Balance</Button>:{" "}<strong style={{ fontSize: 13, color: "black" }}>{balance}</strong>{" "}
      <Button onClick={getUserNFT}>NFT</Button>:{" "}
      <strong style={{ fontSize: 13, color: "black" }}><a href={NFTuri} target="_blank">{NFTuri}</a></strong>
      <Button id="BTN_toWeb3" onClick={connectWallet}></Button>
      <Button id="Write_toWeb3" onClick={WriteUserNFT}></Button>
      </div>
    </div>    
  );
};

export default Home;