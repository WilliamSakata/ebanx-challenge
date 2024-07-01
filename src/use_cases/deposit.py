from src.use_cases import UseCase
from src.entities.Account import account
from src.dtos.deposit import DepositCommand
from src.repository import account as repository

class Deposit(UseCase):
    def execute(command: DepositCommand):
        db_account = repository.find(command.account_id)

        if db_account is None:
            entity = command.to_entity()
            repository.save(entity)
            return entity

        new_balance = float(db_account.balance) + float(command.amount)
        
        new_entity = account(db_account.id, new_balance)

        repository.save(new_entity)

        return new_entity