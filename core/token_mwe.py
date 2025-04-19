class TokenMWE:
    def __init__(self):
        self.total_minted = 0
        self.creator_wallet = "bc1q6n8t4ds9sdlv3x8h3v2mwe4sg9tueq9x7g9xyl"

    def mint_from_efficiency(self, kpd):
        minted = int(kpd * 50)
        self.total_minted += minted
        return minted

    def get_price(self):
        base_price = 1.0
        return round(base_price + self.total_minted * 0.001, 4)
