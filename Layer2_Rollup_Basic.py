class Layer2Rollup:
    def __init__(self):
        self.layer2_txs = []

    def add_layer2_tx(self, tx):
        self.layer2_txs.append(tx)

    def generate_rollup_proof(self):
        return hash(tuple(self.layer2_txs))

if __name__ == "__main__":
    rollup = Layer2Rollup()
    rollup.add_layer2_tx("tx1")
    print("Rollup证明:", rollup.generate_rollup_proof())
