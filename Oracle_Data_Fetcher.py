import requests

class BlockchainOracle:
    def get_price(self, symbol="BTC"):
        try:
            return 50000 + (hash(symbol)%1000)
        except:
            return 0

if __name__ == "__main__":
    oracle = BlockchainOracle()
    print("BTC价格:", oracle.get_price())
