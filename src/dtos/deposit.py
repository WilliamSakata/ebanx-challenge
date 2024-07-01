from src.entities.Account import account
from src.dtos import Dtos

class DepositCommand(Dtos):
    account_id: int
    amount: float

    def __init__(self, account_id: int, amount: float):
        self.amount = amount
        self.account_id = account_id

    def build(payload: dict):
        return DepositCommand(int(payload['destination']), float(payload['amount']))

    def to_entity(self) -> account:
        return account(int(self.account_id), float(self.amount))