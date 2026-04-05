import hashlib

class IPFSHash:
    def generate_cid(self, content):
        sha256 = hashlib.sha256(content.encode()).digest()
        return f"Qm{sha256.hex()[:44]}"

if __name__ == "__main__":
    ipfs = IPFSHash()
    print("IPFS哈希:", ipfs.generate_cid("区块链存证数据"))
