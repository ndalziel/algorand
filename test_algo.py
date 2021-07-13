
from algosdk import account, mnemonic
import json
from algosdk.v2client import algod
from send_tokens import *

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))


receive_mnemonic_secret = "chase hockey clock mobile film salute copper dove list ranch square garlic wonder analyst wide attack wonder resemble museum silly exile emerge fever able robust"
receive_pk = mnemonic.to_public_key(receive_mnemonic_secret)

send_mnemonic_secret = "smile pave injury portion toy few route measure joke immune hard market aim member host chapter security fluid borrow powder total inch husband above cake"
send_pk = mnemonic.to_public_key(send_mnemonic_secret)


def print_balance(pk):
    algod_address = "https://testnet-algorand.api.purestake.io/ps2"
    algod_token = "bk83siccgs6BFY3YaAvX2UrAmPWeHU01PmlC0dk0"
    headers = {
    "X-API-Key": algod_token,
    }
    algod_client = algod.AlgodClient(algod_token, algod_address, headers)
    account_info = algod_client.account_info(pk)
    #account = json.dumps(account_info, indent=4)
    print (pk,account_info['amount'])

response = send_tokens( receive_pk, 100000)
print(response)
print_balance(send_pk)
print_balance(receive_pk)