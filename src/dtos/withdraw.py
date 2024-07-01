from src.entities.Account import account
from src.dtos import Dtos

class WithdrawCommand(Dtos):
    account_id = 0
    amount = 0.0

    def __init__(self, account_id: int, amount: float):
        self.amount = amount
        self.account_id = account_id

    def build(payload: dict):
        return WithdrawCommand(int(payload['origin']), float(payload['amount']))
    
    def to_entity(self) -> account:
        return account(int(self.account_id), float(self.amount))