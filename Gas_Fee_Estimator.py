class GasEstimator:
    def estimate_gas(self, tx_type="transfer"):
        base = 21000
        if tx_type == "contract":
            base += 50000
        return base

if __name__ == "__main__":
    gas = GasEstimator()
    print("转账Gas:", gas.estimate_gas())
