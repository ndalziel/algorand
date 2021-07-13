#!/usr/bin/python3

from algosdk.v2client import algod
from algosdk import mnemonic
from algosdk import transaction
from algosdk import account
from algosdk.future.transaction import PaymentTxn

#Connect to Algorand node maintained by PureStake
#Connect to Algorand node maintained by PureStake
algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_token = "B3SU4KcVKi94Jap2VXkK83xx38bsv95K5UZm2lab"
#algod_token = 'IwMysN3FSZ8zGVaQnoUIJ9RXolbQ5nRY62JRqF2H'
headers = {
   "X-API-Key": algod_token,
}

acl = algod.AlgodClient(algod_token, algod_address, headers)
min_balance = 100000 #https://developer.algorand.org/docs/features/accounts/#minimum-balance

def send_tokens( receiver_pk, tx_amount ):
    #####################################
    #
    # Sends “amount” microalgos to the account given by “receiver_pk” and submit the transaction to the Algorand Testnet.
    #
    #####################################

    params = acl.suggested_params()
    gen_hash = params.gh
    first_valid_round = params.first
    tx_fee = params.min_fee
    last_valid_round = params.last

    mnemonic_secret = "smile pave injury portion toy few route measure joke immune hard market aim member host chapter security fluid borrow powder total inch husband above cake"
    sender_pk = mnemonic.to_public_key(mnemonic_secret)
    sender_sk = mnemonic.to_private_key(mnemonic_secret)
    
    #create a payment transaction
    params = acl.suggested_params()
    receiver = "GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A"
    note = "Testing".encode()
    unsigned_txn = PaymentTxn(sender_pk, params, receiver_pk, tx_amount, None, note)

    # sign the transaction
    signed_txn = unsigned_txn.sign(sender_sk)

    #submit the transaction
    txid = acl.send_transaction(signed_txn)

    return sender_pk, txid

# Function from Algorand Inc.
def wait_for_confirmation(client, txid):
    """
    Utility function to wait until the transaction is
    confirmed before proceeding.
    """
    last_round = client.status().get('last-round')
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
        print("Waiting for confirmation")
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print("Transaction {} confirmed in round {}.".format(txid, txinfo.get('confirmed-round')))
    return txinfo