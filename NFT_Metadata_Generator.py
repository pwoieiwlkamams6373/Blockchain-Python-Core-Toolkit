import json
import hashlib

class NFTMetadata:
    def create_metadata(self, name, desc, image_url, attributes):
        metadata = {
            "name": name,
            "description": desc,
            "image": image_url,
            "attributes": attributes,
            "created_at": "2026-04-05"
        }
        return metadata

    def hash_metadata(self, metadata):
        return hashlib.sha256(json.dumps(metadata).encode()).hexdigest()

if __name__ == "__main__":
    nft = NFTMetadata()
    meta = nft.create_metadata("TestNFT", "测试NFT", "ipfs://xxx", [{"rarity":"rare"}])
    print("NFT哈希:", nft.hash_metadata(meta))
