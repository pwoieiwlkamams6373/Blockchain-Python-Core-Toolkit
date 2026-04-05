class BridgeMonitor:
    def check_liquidity(self, pools, min_liquidity=1000):
        return [k for k,v in pools.items() if v>=min_liquidity]

if __name__ == "__main__":
    monitor = BridgeMonitor()
    print(monitor.check_liquidity({"pool1":500,"pool2":1500}))
