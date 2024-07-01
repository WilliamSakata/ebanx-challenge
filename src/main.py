from fastapi import FastAPI, status, HTTPException
from src.queries.balance import Balance as balance_query
from src.use_cases import use_case_handler
from src.exceptions.AccountNotFound import AccountNotFound

app = FastAPI()

@app.get("/balance/")
async def get_balance(account_id: int):
    try:
        balance = balance_query.get_balance(account_id)
        return balance
    except AccountNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.post("/event", status_code=status.HTTP_201_CREATED)
async def register(command: dict):
    try:
        return use_case_handler.handle(command)
    except AccountNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
