from fastapi import FastAPI, status, HTTPException, Response
from src.queries.balance import Balance as balance_query
from src.use_cases import use_case_handler
from src.repository import account as repository
from src.exceptions.AccountNotFound import AccountNotFound
from src.exceptions.InvalidUseCaseType import InvalidUseCaseType

app = FastAPI()

@app.get("/balance")
async def get_balance(account_id: str):
    try:
        balance = balance_query.get_balance(account_id)
        return balance
    except AccountNotFound as e:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="0")

@app.post("/event", status_code=status.HTTP_201_CREATED)
async def register(command: dict):
    try:
        return use_case_handler.handle(command)
    except AccountNotFound as e:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="0")
    except InvalidUseCaseType as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
@app.post("/reset")
async def reset():
    repository.reset()
    return Response(status_code=status.HTTP_200_OK, content="OK")