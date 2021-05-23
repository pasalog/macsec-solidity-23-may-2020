import json
from web3 import Web3
from rich.console import Console

console = Console()


class MyName:
    def __init__(self):
        self.ganache_url = "http://127.0.0.1:7545"
        self.web3 = Web3(Web3.HTTPProvider(self.ganache_url))
        self.contract = self.start_creation()

    def start_creation(self):
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        art_file = open('build/contracts/MyName.json')
        artifact = json.load(art_file)
        console.log(artifact)
        abi = artifact['abi']
        bytecode = artifact['bytecode']
        tx_hash = self.web3.eth.contract(abi=abi, bytecode=bytecode).constructor().transact()
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return self.web3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=abi
        )

    def say_my_name(self):
        message = self.contract.functions.sayMyName().call()
        return message

    def setMyName(self, name: str):
        return 'test'
