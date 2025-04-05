from pydantic import BaseModel
from fastapi import FastAPI
from typing import List, Optional


app = FastAPI()

class Users(BaseModel):
    id: Optional[int] = None  # Simula una llave primaria
    nombre: str
    apellido: str

# Base de datos simulada (lista en memoria)
db: List[Users] = []

@app.post("/users/")
def add_user(user: Users):
    user.id = len(db) + 1  # Genera ID auto-incremental
    db.append(user)
    return user

@app.get("/users/", response_model=List[Users])
def get_users():
    return db