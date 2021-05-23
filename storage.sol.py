import json
from web3 import Web3
from rich.console import Console

console = Console()

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.isConnected()

web3.eth.defaultAccount = web3.eth.accounts[0]

art_file = open('build/contracts/Storage.json')
artifact = json.load(art_file)

console.log(artifact)
abi = artifact['abi']
bytecode = artifact['bytecode']

Storage = web3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Storage.constructor().transact()

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

console.log(f"Contract creation started.. {tx_receipt.contractAddress}", style="bold blue")
contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# print(contract.functions.store().call())

tx_hash = contract.functions.store(255).transact()

console.log(contract.functions.store(255).call(), style="bold blue")
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

console.log(contract.functions.retrieve().call(), style="bold red")
