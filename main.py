# import json

import json
from web3 import Web3
from solcx import compile_standard, install_solc
from dotenv import load_dotenv
load_dotenv()
import os
from web3.middleware import geth_poa_middleware


class Main:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(os.getenv('HTTP_PROVIDER')))
        self.chain_id = os.getenv('CHAIN_ID')
        self.my_address = os.getenv('MY_ADDRESS')
        self.private_key = os.getenv('MY_PRIVATE_KEY')
        self.IPFSBaseURL = os.getenv('IPFS_BASE_URL')

    def readContract(self):
        with open("./NFT.sol", "r") as file:
            self.contractContent = file.read()
        
    def initCompileStandard(self):
        print("Installing...")
        install_solc("0.8.18")
    
        self.compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"NFT.sol": {"content": self.contractContent}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.18"
)   
        
    def compileSolc(self):
        with open("compiled_code.json", "w") as file:
            json.dump(self.compiled_sol, file, ensure_ascii = True)
            print('compiled solidity code')
            
    def getABI(self):
         with open("compiled_code.json", "r") as file:
             compiled_sol = json.loads(file.read())
             bytecode = compiled_sol["contracts"]["NFT.sol"]["NFT"]["evm"]["bytecode"]["object"]
             self.abi = json.loads(compiled_sol["contracts"]["NFT.sol"]["NFT"]["metadata"])["output"]["abi"]  
             self.NFT = self.w3.eth.contract(abi=self.abi, bytecode=bytecode)
             self.nonce = self.w3.eth.get_transaction_count(self.my_address)


    def deploy(self):
       transaction = self.NFT.constructor("sib nft", "III", 1).build_transaction(
            {
                "chainId": int(self.chain_id),
                "gasPrice": self.w3.eth.gas_price,
                "from": self.my_address,
                "nonce": self.nonce,
            }
        )
       
       self.signed_txn = self.w3.eth.account.sign_transaction(transaction, private_key=self.private_key)
       print("Deploying Contract!")
       self.tx_hash = self.w3.eth.send_raw_transaction(self.signed_txn.rawTransaction)
       print("Waiting for transaction to finish...")
       self.tx_receipt = self.w3.eth.wait_for_transaction_receipt(self.tx_hash)
       print(f"Done! Contract deployed to {self.tx_receipt.contractAddress}")
       
       
    def intractDeployed(self):
        an_nft = self.w3.eth.contract(address=self.tx_receipt.contractAddress, abi=self.abi)
        greeting_transaction = an_nft.functions.mint(self.IPFSBaseURL).build_transaction(
        {
            "chainId": int(self.chain_id),
            "gasPrice": self.w3.eth.gas_price,
            "from": self.my_address,
            "nonce": self.nonce + 1,
            'value': 1,
        })
        
        print(greeting_transaction)
        signed_greeting_txn = self.w3.eth.account.sign_transaction(
            greeting_transaction, private_key=self.private_key
        )
        print(signed_greeting_txn)
        tx_greeting_hash = self.w3.eth.send_raw_transaction(
            signed_greeting_txn.rawTransaction)

        print(tx_greeting_hash)
        print("Updating stored Value...")


obj = Main()
obj.readContract()
obj.initCompileStandard()
obj.compileSolc()
obj.getABI()
obj.deploy()
obj.intractDeployed()