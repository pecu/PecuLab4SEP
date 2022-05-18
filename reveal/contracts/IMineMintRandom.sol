// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;


interface IMineMintRandom {

    /**
     * Requests randomness for the mint purity
     */
    function getRandomMintPurity(uint256 tokenId) external;

}