from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def main():
    return {"Message": "Hello world"}
