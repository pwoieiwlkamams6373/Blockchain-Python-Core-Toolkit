class StakingReward:
    def __init__(self, apy=0.12):
        self.apy = apy

    def calculate_reward(self, stake, days):
        reward = stake * self.apy * (days/365)
        return round(reward,4)

if __name__ == "__main__":
    staking = StakingReward(0.15)
    print("质押收益:", staking.calculate_reward(10000,30))
