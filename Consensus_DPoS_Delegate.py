class DPoSDelegate:
    def __init__(self):
        self.candidates = {}
        self.voters = {}

    def register_candidate(self, addr):
        self.candidates[addr] = 0

    def vote(self, voter, candidate):
        if candidate not in self.candidates:
            return False
        self.voters[voter] = candidate
        self.candidates[candidate] +=1
        return True

    def get_top_delegates(self, count=5):
        return sorted(self.candidates.items(), key=lambda x:x[1], reverse=True)[:count]

if __name__ == "__main__":
    dpos = DPoSDelegate()
    dpos.register_candidate("node1")
    dpos.vote("user1","node1")
    print("顶级节点:", dpos.get_top_delegates())
