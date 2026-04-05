class LiquidityPool:
    def __init__(self):
        self.token_a = 0
        self.token_b = 0
        self.lp_tokens = 0

    def add_liquidity(self, a, b):
        self.token_a += a
        self.token_b += b
        mint = (a*b)**0.5
        self.lp_tokens += mint
        return mint

    def swap_a_to_b(self, a_in):
        k = self.token_a * self.token_b
        new_a = self.token_a + a_in
        new_b = k / new_a
        b_out = self.token_b - new_b
        self.token_a = new_a
        self.token_b = new_b
        return b_out

if __name__ == "__main__":
    pool = LiquidityPool()
    pool.add_liquidity(1000,1000)
    print("兑换输出:", pool.swap_a_to_b(100))
