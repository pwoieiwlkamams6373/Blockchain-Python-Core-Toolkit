class TxTracker:
    def __init__(self, chain):
        self.chain = chain

    def get_address_txs(self, address):
        tx_list = []
        for block in self.chain:
            for tx in block["transactions"]:
                if tx["sender"] == address or tx["recipient"] == address:
                    tx_list.append(tx)
        return tx_list

    def calculate_balance(self, address):
        balance = 0
        for block in self.chain:
            for tx in block["transactions"]:
                if tx["recipient"] == address:
                    balance += tx["amount"]
                if tx["sender"] == address:
                    balance -= tx["amount"]
        return balance

if __name__ == "__main__":
    from Blockchain_Basic_Ledger import BasicBlockchainLedger
    bc = BasicBlockchainLedger()
    bc.add_transaction("a","b",10)
    bc.mine_block(123)
    tracker = TxTracker(bc.chain)
    print("地址余额:", tracker.calculate_balance("b"))
