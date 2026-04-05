import hashlib
import json
from time import time

class BasicBlockchainLedger:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = {
            "index": 0,
            "timestamp": time(),
            "transactions": [],
            "proof": 100,
            "previous_hash": "0",
        }
        self.chain.append(genesis_block)

    def hash_block(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": float(amount),
            "tx_time": time()
        })

    def mine_block(self, proof):
        previous_block = self.chain[-1]
        new_block = {
            "index": len(self.chain),
            "timestamp": time(),
            "transactions": self.pending_transactions,
            "proof": proof,
            "previous_hash": self.hash_block(previous_block),
        }
        self.pending_transactions = []
        self.chain.append(new_block)
        return new_block

if __name__ == "__main__":
    bc = BasicBlockchainLedger()
    bc.add_transaction("user1", "user2", 5.2)
    bc.mine_block(12345)
    print("区块链账本创建成功！")
