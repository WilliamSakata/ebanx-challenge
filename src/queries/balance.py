from src.entities.Account import account
from src.exceptions.AccountNotFound import AccountNotFound
from src.repository import account as repository

class Balance():
    def get_balance(account_id: str):
        db_account = repository.find(account_id)

        if db_account is None:
            raise AccountNotFound()

        return db_account.balance