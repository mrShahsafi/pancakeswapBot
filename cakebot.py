from web3 import Web3
# import json

from config import (
    NETWORK_PROVIDER,
    WRAPPED_BNB,
    PANCAKE_ROUTER_CONTRACT_ADDRESS,
    ETHER_PUBLIC_KEY,
    ETHER_PRIVATE_KEY,
    PANCAKE_ABI,
    TOKEN_CONTRACT_ADDRESS,
)

import time

bsc = NETWORK_PROVIDER
web3 = Web3(Web3.HTTPProvider(bsc))

print(web3.isConnected())

# pancake swap router
panRouterContractAddress = PANCAKE_ROUTER_CONTRACT_ADDRESS

# pancake swap router abi
panabi = PANCAKE_ABI

sender_address = ETHER_PUBLIC_KEY

balance = web3.eth.get_balance(sender_address)
# print(f'balance {balance}')

humanReadable = web3.fromWei(balance, 'ether')
# print(f' in USD balance {humanReadable}')

# Contract Address of Token we want to buy
tokenToBuy = web3.toChecksumAddress(TOKEN_CONTRACT_ADDRESS)

spend = web3.toChecksumAddress(WRAPPED_BNB)  # w_bnb contract

# Setup the PancakeSwap contract
contract = web3.eth.contract(address = panRouterContractAddress, abi = panabi)

nonce = web3.eth.get_transaction_count(sender_address)

start = time.time()

pancakeswap2_txn = contract.functions.swapExactETHForTokens(
    10000000000,  # set to 0, or specify minimum amount of tokeny you want to receive - consider decimals!!!
    [spend, tokenToBuy],
    sender_address,
    (int(time.time()) + 10000)
).buildTransaction({
    'from': sender_address,
    'value': web3.toWei(0.001, 'ether'),  # This is the Token(BNB) amount you want to Swap from
    'gas': 250000,
    'gasPrice': web3.toWei('5', 'gwei'),
    'nonce': nonce,
})

signed_txn = web3.eth.account.sign_transaction(
    pancakeswap2_txn, private_key = ETHER_PRIVATE_KEY
)
try:
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print(web3.toHex(tx_token))
except ValueError as e:

    print(f'{e}')