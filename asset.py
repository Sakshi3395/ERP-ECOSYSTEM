class Asset:
    def __init__(self, asset_id, name, value):
        self.asset_id = asset_id
        self.name = name
        self.value = value

    def depreciate(self, years):
        return self.value * (0.9 ** years)

    def __str__(self):
        return f"ID: {self.asset_id} | {self.name} | Value: ₹{self.value}"

class Hardware(Asset):
    def __init__(self, asset_id, name, value, condition):
        super().__init__(asset_id, name, value)
        self.condition = condition
        self.asset_type = "Hardware"

class Software(Asset):
    def __init__(self, asset_id, name, value, expiry_date):
        super().__init__(asset_id, name, value)
        self.expiry_date = expiry_date
        self.asset_type = "Software"