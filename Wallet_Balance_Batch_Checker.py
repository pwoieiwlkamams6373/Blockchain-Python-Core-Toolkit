class BatchChecker:
    def __init__(self, chain):
        self.chain = chain

    def batch_balance(self, addresses):
        res = {}
        for addr in addresses:
            balance = 0
            for b in self.chain:
                for tx in b["transactions"]:
                    if tx["recipient"]==addr: balance+=tx["amount"]
                    if tx["sender"]==addr: balance-=tx["amount"]
            res[addr] = balance
        return res

if __name__ == "__main__":
    from Blockchain_Basic_Ledger import BasicBlockchainLedger
    checker = BatchChecker(BasicBlockchainLedger().chain)
    print(checker.batch_balance(["a","b"]))
