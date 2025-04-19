from token import TokenMWE

class BalanceManager:
    def __init__(self, token: TokenMWE):
        self.token = token

    def get_balance(self, address):
        balance = self.token.balance_of(address)
        return balance / (10 ** self.token.decimals)

    def is_whale(self, address, threshold=10000):
        return self.get_balance(address) >= threshold

    def get_creator_balance(self):
        return self.get_balance(self.token.creator_wallet)
