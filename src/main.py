from fastapi import FastAPI, status, HTTPException
from src.use_cases import use_case_handler
from src.exceptions.AccountNotFound import AccountNotFound

app = FastAPI()

@app.post("/event", status_code=status.HTTP_201_CREATED)
async def register(command: dict):
    try:
        return use_case_handler.handle(command)
    except AccountNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
