class NFTStaking:
    def __init__(self, reward_per_day=10):
        self.reward = reward_per_day
        self.staked = {}

    def stake(self, nft_id, addr):
        self.staked[nft_id] = addr

    def claim_reward(self, nft_id, days):
        return self.reward * days

if __name__ == "__main__":
    nft_stake = NFTStaking()
    nft_stake.stake(1001,"user")
    print("奖励:", nft_stake.claim_reward(1001,7))
