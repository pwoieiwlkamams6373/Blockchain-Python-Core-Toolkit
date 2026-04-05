class SimpleERC20:
    def __init__(self, name, symbol, total_supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balances = {}
        self.balances["owner"] = total_supply

    def transfer(self, sender, recipient, amount):
        if self.balances.get(sender, 0) < amount:
            return False
        self.balances[sender] -= amount
        self.balances[recipient] = self.balances.get(recipient, 0) + amount
        return True

    def balance_of(self, address):
        return self.balances.get(address, 0)

if __name__ == "__main__":
    token = SimpleERC20("TestToken", "TTK", 1000000)
    token.transfer("owner", "user1", 1000)
    print("user1余额:", token.balance_of("user1"))
