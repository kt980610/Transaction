from web3 import Web3
ganache_url="http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
account1_public_key = '0x89f0611f0f14f1f7c264a89C2e6bA8F2222637c0'
account2_public_key = '0x2C949b564251039f435c733110aB77DaC34538bd'
account1_private_key = 'fe5ab43bd5048755f2518e7cf1a77e96db68544d0763f29a32e74a85b1c22072'
nonce=web3.eth.getTransactionCount(account1_public_key)

tx = {
    'nonce': nonce,
    'to': account2_public_key,
    'value': web3.toWei(5,'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei(50,'gwei')
}
signed_tx = web3.eth.account.signTransaction(tx,account1_private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))









