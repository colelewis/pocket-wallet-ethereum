from hd_engine import *

mnemonic_root = Mnemonic("english")
mnemonic = mnemonic_root.generate(strength=256) #128 = 12 words, 256 = 24 words

private_key = mnemonic_to_private_key(mnemonic, "")
public_key = PublicKey(private_key)

print(f'\nprivkey: {binascii.hexlify(private_key).decode("utf-8")}\n')
print(f'pubkey:  {binascii.hexlify(bytes(public_key)).decode("utf-8")}\n')
print(f'address: {public_key.address()}\n')
print("Mnemonic: {}\n".format(mnemonic))