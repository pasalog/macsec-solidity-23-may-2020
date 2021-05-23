import json
from web3 import Web3
from rich.console import Console

console = Console()

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.isConnected()

web3.eth.defaultAccount = web3.eth.accounts[0]

art_file = open('build/contracts/MyName.json')
artifact = json.load(art_file)

console.log(artifact)

abi = artifact['abi']

bytecode = artifact['bytecode']

SayMyName = web3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = SayMyName.constructor().transact()

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

message = contract.functions.sayMyName().call()

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

console.log(message, style="bold red")
