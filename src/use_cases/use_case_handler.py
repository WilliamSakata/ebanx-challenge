from src.use_cases.deposit import Deposit
from src.use_cases.withdraw import Withdraw
from src.dtos.deposit import DepositCommand
from src.dtos.withdraw import WithdrawCommand

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
        return {"message": "Transfer received!"}
    
    