from eth_account import Account
import secrets


def generate_eth_wallet():
    hash = secrets.token_hex(32)
    private_key = "0x" + hash
    # print("SAVE BUT DO NOT SHARE THIS:", private_key)
    account = Account.from_key(private_key)
    # print("Address:", acct.address)
    return account.address, private_key
