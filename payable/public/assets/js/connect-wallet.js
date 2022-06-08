const ethereumButton = document.querySelector('.enableEthereumButton');
const ethereumButtonBody = document.querySelector('.enableEthereumButtonBody');

ethereumButton.addEventListener('click', () => {
    //Will Start the metamask extension
    ethereum.request({ method: 'eth_requestAccounts' });
});

ethereumButtonBody.addEventListener('click', () => {
    //Will Start the metamask extension
    ethereum.request({ method: 'eth_requestAccounts' });
});