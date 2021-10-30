from web3 import Web3
# import json

from config import (
    ETH_NETWORK_PROVIDER,
    BSC_NETWORK_PROVIDER,
    TRX_NETWORK_PROVIDER,
    WRAPPED_BNB,
    PANCAKE_ROUTER_CONTRACT_ADDRESS,
    ETHER_PUBLIC_KEY,
    ETHER_PRIVATE_KEY,
    PANCAKE_ABI,
    TOKEN_CONTRACT_ADDRESS,
)
from walletGenerator import generate_eth_wallet

import time


def exchange_maker(
        network='bsc',
        token_contract=TOKEN_CONTRACT_ADDRESS,
        amount=0.00001905
):
    if network == 'eth':
        web3 = Web3(Web3.HTTPProvider(ETH_NETWORK_PROVIDER))
    elif network == 'bsc':
        web3 = Web3(Web3.HTTPProvider(BSC_NETWORK_PROVIDER))
    else:
        web3 = Web3(Web3.HTTPProvider(TRX_NETWORK_PROVIDER))

    print(web3.isConnected())

    # pancake swap router
    pan_router_contract_address = PANCAKE_ROUTER_CONTRACT_ADDRESS

    # pancake swap router abi
    panabi = PANCAKE_ABI

    sender_address = ETHER_PUBLIC_KEY

    balance = web3.eth.get_balance(sender_address)
    print(f'balance {balance}')

    # humanReadable = web3.fromWei(balance, 'ether')
    # print(f' in USD balance {humanReadable}')

    # Contract Address of Token we want to buy
    token_to_buy = web3.toChecksumAddress(token_contract)
    print(f'token address {token_contract}')
    spend = web3.toChecksumAddress(WRAPPED_BNB)  # w_bnb contract

    # Setup the PancakeSwap contract
    contract = web3.eth.contract(
        address = pan_router_contract_address,
        abi = panabi
    )

    nonce = web3.eth.get_transaction_count(
        sender_address
    )
    print(f'nonce {nonce}')
    start = time.time()

    receiver_address, receiver_address_private_key = generate_eth_wallet()

    print(f'wallet: {receiver_address}, key: {receiver_address_private_key}')

    pancake_swap2_txn = contract.functions.swapExactETHForTokens(
        10000000000,  # set to 0, or specify minimum amount of token you want to receive - consider decimals!!!
        [spend, token_to_buy],
        receiver_address,  # the receiver address, you can set your sender wallet.
        (int(start) + 10000)
    ).buildTransaction({
        'from': sender_address,
        'value': web3.toWei(amount, 'ether'),  # This is the Token(BNB) amount you want to Swap from
        'gas': 250000,
        'gasPrice': web3.toWei('5', 'gwei'),
        'nonce': nonce,
    })
    # sending purchased token to the wallet

    signed_txn = web3.eth.account.sign_transaction(
        pancake_swap2_txn,
        private_key = ETHER_PRIVATE_KEY
    )
    try:
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        print(web3.toHex(tx_token))
        return True
    except ValueError as e:
        print(f'{e}')
        return False
