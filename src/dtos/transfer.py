from typing import Dict
from src.entities.Account import account
from src.dtos import Dtos

class TransferCommand(Dtos):
    origin: str
    destination: str
    amount: int

    def __init__(self, origin: str, destination: str, amount: int):
        self.amount = amount
        self.origin = origin
        self.destination = destination

    def build(payload: dict):
        return TransferCommand(payload['origin'], payload['destination'], int(payload['amount']))