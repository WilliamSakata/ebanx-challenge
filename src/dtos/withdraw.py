from src.entities.Account import account
from src.dtos import Dtos

class WithdrawCommand(Dtos):
    account_id: str
    amount: int

    def __init__(self, account_id: int, amount: int):
        self.amount = amount
        self.account_id = account_id

    def build(payload: dict):
        return WithdrawCommand(payload['origin'], int(payload['amount']))