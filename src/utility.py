from web3 import Web3
from cryptoaddress import EthereumAddress
from web3.auto import w3
from web3.eth import Eth
#from src import hd_engine
import eth_keyfile, sys, os, json

web3 = Web3(Web3.WebsocketProvider('ws://192.168.0.142:3334'))
#web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545')) #when ganache is active

DEFAULT_FOLDER_PATH = os.path.expanduser("~/.pocket-eth")


def get_address_balance(address):
    balance = web3.eth.get_balance(address)
    try:
        return('{} ETH'.format(web3.fromWei(balance, 'ether')))
    except ValueError:
        print('Invalid address.')

def add_transaction_to_history(): #to be done with making transactions
    pass

def create_wallet(wallet_name):
    #stores the wallet directory with name to the user's default home directory
    os.makedirs(os.path.expanduser(DEFAULT_FOLDER_PATH + '/wallets/{}'.format(wallet_name)), exist_ok=True)

def any_wallets():
    return os.path.isdir(DEFAULT_FOLDER_PATH)
    
def write_private_key_to_wallet(private_key, wallet_name, passphrase):
    #path = os.path.expanduser(DEFAULT_FOLDER_PATH + '/wallets/{}'.format(wallet_name) + '/keystore.json')
    try:
        #private_key_encrypted_json = open(path, "w")
        with open(os.path.expanduser(DEFAULT_FOLDER_PATH + '/wallets/{}'.format(wallet_name) + '/keystore.json'), 'w') as private_keystore_json:
            private_keystore_json.write(json.dumps(eth_keyfile.create_keyfile_json(private_key, b'passphrase')))
            private_keystore_json.close()
    except FileNotFoundError:
        print('Wallet directory does not exist.')

def derive_private_key_from_wallet(wallet_name, passphrase):
    os.path.expanduser(DEFAULT_FOLDER_PATH + '/wallets/{}'.format(wallet_name) + '/keystore.json')
    return (eth_keyfile.extract_key_from_keyfile(os.path.expanduser(DEFAULT_FOLDER_PATH + '/wallets/{}'.format(wallet_name) + '/keystore.json'), b'passphrase'))

def send_transaction(recipient, sender, value, gas, max_fee_per_gas, max_priority_fee_per_gas): #compliant with EIP-1559, https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md
    try:
        web3.eth.send_transaction({
        'to': recipient,
        'from': sender,
        'value': value,
        'gas': gas,
        'maxFeePerGas': max_fee_per_gas, 
        'maxPriorityFeePerGas': max_priority_fee_per_gas
    }) #maxFeePerGas and maxPriorityFeePerGas are both currently defaulted as empty to allow for automatic calculation without pre-defined defaults
    except ValueError:
        print('Invalid address(es). Please check the sender and recipient addresses and verify.')
