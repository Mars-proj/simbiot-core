import time

class Staking:
    def __init__(self, token):
        self.token = token
        self.stakes = {}
        self.rewards = {}

    def stake(self, address, amount):
        scaled = int(amount * (10 ** self.token.decimals))
        if self.token.balances.get(address, 0) < scaled:
            return False
        self.token.balances[address] -= scaled
        self.stakes[address] = {
            "amount": scaled,
            "start": time.time()
        }
        return True

    def calculate_reward(self, address):
        if address not in self.stakes:
            return 0
        duration = time.time() - self.stakes[address]["start"]
        reward = (self.stakes[address]["amount"] / 1e8) * (duration / 86400) * 0.05
        return round(reward, 8)

    def claim(self, address):
        reward = self.calculate_reward(address)
        self.token.mint(address, reward)
        self.stakes[address]["start"] = time.time()
        return reward
