class BlockOptimizer:
    def optimize_block(self, txs, max_size=1024):
        current = 0
        res = []
        for tx in txs:
            if current+len(str(tx)) <= max_size:
                res.append(tx)
                current += len(str(tx))
        return res

if __name__ == "__main__":
    opt = BlockOptimizer()
    print(opt.optimize_block([1,2,3,4],5))
