from typing import Dict
from src.use_cases import UseCase
from src.entities.Account import account
from src.dtos.transfer import TransferCommand
from src.repository import account as repository
from src.exceptions.AccountNotFound import AccountNotFound

class Transfer(UseCase):
    def execute(command: TransferCommand) -> Dict[str, account]:
        origin_account = repository.find(command.origin)
        destination_account = repository.find(command.destination)

        if (origin_account is None):
            raise AccountNotFound()
        
        if (destination_account is None):
            destination_account = account(command.destination, 0)
            repository.save(destination_account)

        new_balance_origin = int(origin_account.balance) - int(command.amount)
        new_balance_destination = int(destination_account.balance) + int(command.amount)

        new_origin = account(origin_account.id, new_balance_origin)
        new_destination = account(destination_account.id, new_balance_destination)

        repository.save(new_origin)
        repository.save(new_destination)

        result = dict()

        result["new_origin"] = new_origin
        result["new_destination"] = new_destination

        return result