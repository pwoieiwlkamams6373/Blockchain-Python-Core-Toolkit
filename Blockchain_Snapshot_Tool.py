import json

class SnapshotTool:
    def create_snapshot(self, chain, path="snapshot.json"):
        with open(path,"w") as f:
            json.dump(chain,f)
        return True

if __name__ == "__main__":
    from Blockchain_Basic_Ledger import BasicBlockchainLedger
    snap = SnapshotTool()
    print("快照创建:", snap.create_snapshot(BasicBlockchainLedger().chain))
