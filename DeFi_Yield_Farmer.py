class YieldFarmer:
    def calculate_apr(self, pool_apr, compund_days=365):
        return (1+pool_apr/compund_days)**compund_days -1

if __name__ == "__main__":
    farmer = YieldFarmer()
    print("复合APR:", farmer.calculate_apr(0.2))
