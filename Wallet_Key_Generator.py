import hashlib
import secrets

class BlockchainWallet:
    def generate_private_key(self):
        return secrets.token_hex(32)

    def private_to_public(self, private_key):
        return hashlib.sha256(private_key.encode()).hexdigest()

    def public_to_address(self, public_key):
        hash1 = hashlib.sha256(public_key.encode()).digest()
        hash2 = hashlib.ripemd160(hash1).digest()
        return "0x" + hash2.hex()

if __name__ == "__main__":
    wallet = BlockchainWallet()
    pk = wallet.generate_private_key()
    pub = wallet.private_to_public(pk)
    addr = wallet.public_to_address(pub)
    print(f"私钥:{pk}\n公钥:{pub}\n地址:{addr}")
