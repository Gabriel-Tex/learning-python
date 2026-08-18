from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    active: bool = True

@app.get("/saudar/{nome}")
async def saudar(nome: str):
    return {f"Olá, {nome}!"}

@app.post("/users")
async def createUser(user: User):
    return{
        "message": "Usuário criado.",
        "data": dict(user)
    }

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=3000,
        reload=True
    )

