import hashlib

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = [hashlib.sha256(tx.encode()).hexdigest() for tx in transactions]

    def build_tree(self):
        if len(self.transactions) == 0:
            return ""
        nodes = self.transactions.copy()
        while len(nodes) > 1:
            temp = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i+1] if i+1 < len(nodes) else left
                combined = hashlib.sha256((left+right).encode()).hexdigest()
                temp.append(combined)
            nodes = temp
        return nodes[0]

if __name__ == "__main__":
    txs = ["tx1", "tx2", "tx3", "tx4"]
    mt = MerkleTree(txs)
    print("默克尔根:", mt.build_tree())
