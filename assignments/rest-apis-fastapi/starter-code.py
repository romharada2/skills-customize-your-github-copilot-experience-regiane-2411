from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Armazenamento em memória: id -> item
items = {}

# TODO: defina o modelo Pydantic com name (str), price (float > 0) e in_stock (bool)

# TODO: implemente os endpoints descritos no README
