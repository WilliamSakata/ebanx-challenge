from fastapi import FastAPI
from src.use_cases import use_case_handler

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/event")
async def register(command: dict):
    return use_case_handler.handle(command)
