
class account:
    id: int
    balance: float
    
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def __str__(self):
        return f'{self.name} - {self.balance}'