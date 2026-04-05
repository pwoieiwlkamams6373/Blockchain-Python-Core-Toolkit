class CrossChainBridge:
    def __init__(self):
        self.chain_a_balance = {}
        self.chain_b_balance = {}

    def lock_asset(self, address, amount, chain):
        if chain == "A":
            self.chain_a_balance[address] = self.chain_a_balance.get(address,0) + amount
        elif chain == "B":
            self.chain_b_balance[address] = self.chain_b_balance.get(address,0) + amount

    def unlock_asset(self, address, amount, chain):
        if chain == "A" and self.chain_a_balance.get(address,0)>=amount:
            self.chain_a_balance[address] -= amount
            return True
        elif chain == "B" and self.chain_b_balance.get(address,0)>=amount:
            self.chain_b_balance[address] -= amount
            return True
        return False

if __name__ == "__main__":
    bridge = CrossChainBridge()
    bridge.lock_asset("user", 100, "A")
    print("跨链解锁:", bridge.unlock_asset("user",50,"A"))
