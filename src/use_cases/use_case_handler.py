from src.dtos.deposit_comand import DepositCommand
from src.use_cases import deposit

def handle(payload: dict):
    print(payload)
    if (payload['type'] == 'deposit'):
        command = DepositCommand.build(payload)
        account = deposit.execute(command)

        return {"destination": {"id": account.id, "balance": account.balance}}
    
    if (payload['type'] == 'withdraw'):
        return {"message": "Withdraw received!"}
    
    if (payload['type'] == 'transfer'):
        return {"message": "Transfer received!"}
    
    