class ShardingManager:
    def __init__(self, shards=4):
        self.shards = {i:[] for i in range(shards)}

    def assign_address(self, addr):
        return int(addr,16) % len(self.shards)

if __name__ == "__main__":
    sm = ShardingManager()
    print("分片编号:", sm.assign_address("0x123456"))
