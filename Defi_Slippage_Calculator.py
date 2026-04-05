class SlippageCalculator:
    def calculate(self, amount_in, amount_out, expected_out):
        slippage = abs(amount_out - expected_out)/expected_out
        return round(slippage*100,2)

if __name__ == "__main__":
    slip = SlippageCalculator()
    print("滑点:", slip.calculate(100,95,100),"%")
