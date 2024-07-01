from src.entities.Account import account
from src.dtos import Dtos

class DepositCommand(Dtos):
    account_id: str
    amount: int

    def __init__(self, account_id: int, amount: int):
        self.amount = amount
        self.account_id = account_id

    def build(payload: dict):
        return DepositCommand(payload['destination'], int(payload['amount']))

    def to_entity(self) -> account:
        return account(self.account_id, int(self.amount))