class Asset:
    def __init__(self, asset_id, name, value):
        self.asset_id = asset_id
        self.name = name
        self.value = value

    def depreciate(self, years):
        return self.value * (0.9 ** years)

    def __str__(self):
        return f"{self.asset_id} | {self.name} | ₹{self.value}"


class Hardware(Asset):
    def __init__(self, asset_id, name, value, condition):
        super().__init__(asset_id, name, value)
        self.condition = condition


class Software(Asset):
    def __init__(self, asset_id, name, value, expiry):
        super().__init__(asset_id, name, value)
        self.expiry = expiry