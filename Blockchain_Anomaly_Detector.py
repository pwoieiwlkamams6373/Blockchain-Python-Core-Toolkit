class AnomalyDetector:
    def detect_large_tx(self, txs, threshold=1000):
        return [tx for tx in txs if tx["amount"]>threshold]

if __name__ == "__main__":
    detector = AnomalyDetector()
    print(detector.detect_large_tx([{"amount":500},{"amount":2000}]))
