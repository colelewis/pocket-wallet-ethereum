#built in accordance to the Ethereum Yellow Paper: https://ethereum.github.io/yellowpaper/paper.pdf
#made by Cole Lewis

import secrets, os
from _pysha3 import keccak_256 #Ethereum hashing standard
from coincurve import PublicKey #bindings for libsecp256k1

def generate_private_key():
    #hashes a random 32 byte number with keccak_256
    return keccak_256(secrets.token_bytes(32)).digest()

def derive_public_key(private_key):
    #public key must be a byte array of size 64
    #we get the uncompressed 65 byte key, then strip the 1st byte to get the 64 byte public key
    return(PublicKey.from_valid_secret(private_key).format(compressed=False)[1:])

def derive_ethereum_address(public_key):
    return(keccak_256(public_key).digest()[-20:])
    #takes the rightmost 20 bytes of the 32 byte keccak hash from the ECDSA public key 
    #note: prefix it with 0x

def export_private_key(private_key, file_path):
    directive = os.path.join(path, "private_key.txt")
    private_key_file = open(directive, "x")
    private_key_file.write(private_key.hex())
    private_key_file.close()

def export_public_key(public_key, file_path):
    directive = os.path.join(path, "public_key.txt")
    public_key_file = open(directive, "x")
    public_key_file.write(public_key.hex())
    public_key_file.close()

def import_private_key():
    pass

