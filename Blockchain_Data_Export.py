import csv

class DataExporter:
    def export_chain(self, chain, path="chain.csv"):
        with open(path,"w",newline="") as f:
            w = csv.writer(f)
            w.writerow(["区块高度","时间戳","交易数"])
            for i,b in enumerate(chain):
                w.writerow([i,b["timestamp"],len(b["transactions"])])
        return True

if __name__ == "__main__":
    from Blockchain_Basic_Ledger import BasicBlockchainLedger
    exp = DataExporter()
    print("导出成功:", exp.export_chain(BasicBlockchainLedger().chain))
