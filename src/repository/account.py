from typing import Optional
from src.entities.Account import account

accounts = {}

def find(account_id) -> Optional[account]:
    account = accounts.get(account_id)

    if (account is None):
        return None
    
    return account

def save(account: account):
    accounts[account.id] = account
    return