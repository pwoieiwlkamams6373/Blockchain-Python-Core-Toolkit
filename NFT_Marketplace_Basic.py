class NFTMarketplace:
    def __init__(self):
        self.listings = {}

    def list_nft(self, nft_id, seller, price):
        self.listings[nft_id] = {"seller":seller, "price":price}

    def buy_nft(self, nft_id, buyer):
        if nft_id in self.listings:
            del self.listings[nft_id]
            return True
        return False

if __name__ == "__main__":
    market = NFTMarketplace()
    market.list_nft(1001,"seller",10)
    print("购买结果:", market.buy_nft(1001,"buyer"))
