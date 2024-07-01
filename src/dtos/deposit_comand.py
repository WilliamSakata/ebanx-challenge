from src.entities.Account import account

class DepositCommand:
    account_id = 0
    amount = 0.0

    def __init__(self, amount: float, account_id: int):
        self.amount = amount
        self.account_id = account_id

    def build(payload: dict):
        return DepositCommand(int(payload['destination']), float(payload['amount']))

    def to_entity(self) -> account:
        return account(int(self.account_id), float(self.amount))