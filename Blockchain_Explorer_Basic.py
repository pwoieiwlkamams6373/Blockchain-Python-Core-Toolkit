class BlockchainExplorer:
    def __init__(self, chain):
        self.chain = chain

    def get_block_by_height(self, height):
        if 0<=height<len(self.chain):
            return self.chain[height]
        return None

    def get_latest_block(self):
        return self.chain[-1]

    def get_chain_height(self):
        return len(self.chain)-1

if __name__ == "__main__":
    from Blockchain_Basic_Ledger import BasicBlockchainLedger
    bc = BasicBlockchainLedger()
    exp = BlockchainExplorer(bc.chain)
    print("区块高度:", exp.get_chain_height())
