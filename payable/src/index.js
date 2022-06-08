import React from "react";
import ReactDOM from "react-dom";
import { Dapp } from "./components/Dapp";
import "bootstrap/dist/css/bootstrap.css";

const domContainer = document.querySelector('#nft_index');
ReactDOM.render(
    <React.StrictMode>
    <Dapp />
    </React.StrictMode>,
    domContainer
);