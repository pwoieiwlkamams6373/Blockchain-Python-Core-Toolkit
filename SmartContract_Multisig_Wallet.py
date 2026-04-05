class MultisigWallet:
    def __init__(self, owners, required):
        self.owners = owners
        self.required = required
        self.approvals = {}
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def approve_tx(self, owner, tx_id):
        if owner in self.owners:
            self.approvals[tx_id] = self.approvals.get(tx_id,0)+1

    def execute_tx(self, tx_id, amount):
        if self.approvals.get(tx_id,0)>=self.required and self.balance>=amount:
            self.balance -= amount
            return True
        return False

if __name__ == "__main__":
    wallet = MultisigWallet(["a","b","c"],2)
    wallet.deposit(1000)
    wallet.approve_tx("a","tx1")
    wallet.approve_tx("b","tx1")
    print("执行结果:", wallet.execute_tx("tx1",500))
