import { Web3ReactProvider } from "@web3-react/core";
import { Web3Provider } from "@ethersproject/providers";
import Home from "./pages/Home";

function App() {
  // To get the provider and set into library
  function getLibrary(provider) {
    return new Web3Provider(provider);
  }
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <Home />
    </Web3ReactProvider>
  );
}

export default App;