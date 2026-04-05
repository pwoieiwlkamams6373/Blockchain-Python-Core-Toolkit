class PBFT:
    def __init__(self, nodes=4):
        self.nodes = nodes
        self.required = (2*nodes)//3 +1

    def pre_prepare(self):
        return "pre_prepare"

    def prepare(self):
        return sum([1 for _ in range(self.nodes)]) >= self.required

if __name__ == "__main__":
    pbft = PBFT()
    print("准备阶段完成:", pbft.prepare())
