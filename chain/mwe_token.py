class TokenMWE:
    def __init__(self):
        self.name = "Meredian World Energy"
        self.symbol = "MWE"
        self.decimals = 8
        self.balances = {}
        self.creator_wallet = "bc1q6n8t4ds9sdlv3x8h3v2mwe4sg9tueq9x7g9xyl"

    def mint(self, address, amount):
        amount_scaled = int(amount * (10 ** self.decimals))
        self.balances[address] = self.balances.get(address, 0) + amount_scaled

    def balance_of(self, address):
        return self.balances.get(address, 0)

    def transfer(self, sender, recipient, amount):
        amount_scaled = int(amount * (10 ** self.decimals))
        commission = int(1 * (10 ** self.decimals))
        creator_cut = int(commission * 0.05)

        if self.balances.get(sender, 0) < amount_scaled + commission:
            return False

        self.balances[sender] -= amount_scaled + commission
        self.balances[recipient] = self.balances.get(recipient, 0) + amount_scaled
        self.balances[self.creator_wallet] = self.balances.get(self.creator_wallet, 0) + creator_cut

        return True

    def reward_neuron(self, address, action_strength=1):
        # AI или торговля вызывает это — создаёт энергию
        reward = action_strength * 0.1  # 0.1 MWE за действие
        self.mint(address, reward)
