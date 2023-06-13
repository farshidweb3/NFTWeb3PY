# NFT Contract Deployment

This Python script allows you to deploy an NFT contract on the Ethereum blockchain using the provided Solidity code. The script uses the Web3 library to interact with the Ethereum network and perform the deployment.

## Rarible

[![rarible](favicon.png) Deployed NFT on Rarible](https://testnet.rarible.com/token/polygon/0xd46b694cc339f8273a51a9c71fdbc04dd9fa23cf:0?tab=overview)

[![rarible](deployed_nft.png)](https://testnet.rarible.com/token/polygon/0xd46b694cc339f8273a51a9c71fdbc04dd9fa23cf:0?tab=overview)

## Installation

To use this script, follow these steps:

1. Install Python: Make sure you have Python installed on your system.
2. Install required packages: Run `pip install web3 solcx python-dotenv` to install the necessary dependencies.
3. Set up environment variables: Create a `.env` file and set the following variables:
   - `HTTP_PROVIDER`: The HTTP provider URL for your Ethereum node.
   - `CHAIN_ID`: The chain ID of the Ethereum network you want to deploy to.
   - `MY_ADDRESS`: Your Ethereum address.
   - `MY_PRIVATE_KEY`: Your private key for the Ethereum address.
   - `IPFS_BASE_URL`: The base URL for IPFS to store the NFT token URI.
4. Update Solidity code: Make sure the `NFT.sol` file contains the Solidity code for your NFT contract.
5. Run the script: Execute the Python script to compile the Solidity code, deploy the NFT contract, and interact with the deployed contract to mint an NFT token.

## Technologies Used

- Python: The script is written in Python, a popular programming language.
- Web3: The Web3 library is used to interact with the Ethereum blockchain.
- solcx: The solcx library is used to compile the Solidity code.
- python-dotenv: The python-dotenv library is used to load environment variables from a `.env` file.

## Usage

1. Make sure you have the necessary environment variables set in the `.env` file.
2. Update the `NFT.sol` file with your own Solidity code, if needed.
3. Run the script using `python script.py` or in your preferred Python environment.
4. The script will compile the Solidity code, deploy the contract, and interact with the deployed contract to mint an NFT token.
5. The deployed contract address and transaction hash will be printed once the deployment is successful.
6. Upload json file to IPFS for detail of nft like this

```
{
  "name": "certificate",
  "description": "certificate description",
  "image": "ipfs://bafkreibrsid7ggfh4rvneyyecixj526i2uj7jyb3gn63rqtsjbf4mwglje"
}
```

## License

This project is licensed under the MIT license.

Note: Please make sure to include appropriate error handling and security measures when using this script in a production environment.
