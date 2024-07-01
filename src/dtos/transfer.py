from typing import Dict
from src.entities.Account import account
from src.dtos import Dtos

class TransferCommand(Dtos):
    origin = 0
    destination = 0
    amount = 0.0

    def __init__(self, origin: int, destination: int, amount: float):
        self.amount = amount
        self.origin = origin
        self.destination = destination

    def build(payload: dict):
        return TransferCommand(int(payload['origin']), int(payload['destination']), float(payload['amount']))