from fastapi import FastAPI
from src.domain.entities.customer_entity import CustomerCustomProperties

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
