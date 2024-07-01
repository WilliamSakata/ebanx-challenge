from src.use_cases.deposit import Deposit
from src.use_cases.transfer import Transfer
from src.use_cases.withdraw import Withdraw
from src.dtos.deposit import DepositCommand
from src.dtos.transfer import TransferCommand
from src.dtos.withdraw import WithdrawCommand
from src.exceptions.InvalidUseCaseType import InvalidUseCaseType

def handle(payload: dict):
    if (payload['type'] == 'deposit'):
        command = DepositCommand.build(payload)
        account = Deposit.execute(command)

        return {"destination": {"id": account.id, "balance": account.balance}}
    
    if (payload['type'] == 'withdraw'):
        command = WithdrawCommand.build(payload)

        account = Withdraw.execute(command)

        return {"origin": {"id": account.id, "balance": account.balance}}
    
    if (payload['type'] == 'transfer'):
        command = TransferCommand.build(payload)

        transfer = Transfer.execute(command)

        return {
            "origin": {
                "id": transfer['new_origin'].id, 
                "balance": transfer['new_origin'].balance
            }, 
            "destination": {
                "id": transfer['new_destination'].id, 
                "balance": transfer['new_destination'].balance
            }
        }
    
    raise InvalidUseCaseType()
    
    