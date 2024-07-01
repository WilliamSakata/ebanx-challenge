from src.use_cases import UseCase
from src.entities.Account import account
from src.dtos.withdraw import WithdrawCommand
from src.repository import account as repository
from src.exceptions.AccountNotFound import AccountNotFound

class Withdraw(UseCase):
    def execute(command: WithdrawCommand):
        db_account = repository.find(command.account_id)

        if (db_account is None):
            raise AccountNotFound()
        
        new_balance = float(db_account.balance) - float(command.amount)

        new_entity = account(db_account.id, new_balance)

        repository.save(new_entity)

        return new_entity