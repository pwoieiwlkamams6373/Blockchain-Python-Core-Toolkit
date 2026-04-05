import random

class PoSValidator:
    def __init__(self):
        self.validators = {}

    def register_validator(self, address, stake):
        self.validators[address] = int(stake)

    def select_validator(self):
        total_stake = sum(self.validators.values())
        if total_stake == 0:
            return None
        rand = random.uniform(0, total_stake)
        current = 0
        for addr, stake in self.validators.items():
            current += stake
            if current >= rand:
                return addr
        return None

if __name__ == "__main__":
    pos = PoSValidator()
    pos.register_validator("node1", 100)
    pos.register_validator("node2", 300)
    print("本轮出块节点:", pos.select_validator())
