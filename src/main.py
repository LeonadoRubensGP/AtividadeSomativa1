from fastapi import FastAPI
import random
from pydantic import BaseModel

app = FastAPI()


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool



# http://127.0.0.1:8000/
@app.get("/")
async def root():
    """Retorna uma mensagem simples de boas-vindas."""
    return {"message": "Hello World"}

# http://127.0.0.1:8000/teste
@app.get("/teste")
async def funcaoteste():
    """Retorna uma mensagem simples de boas-vindas."""
    return {"message": "função de teste 1"}

# http://127.0.0.1:8000/outrospontos
@app.get("/outrospontos")
async def funcaoteste():
    """Retorna uma mensagem simples de boas-vindas."""
    return {"message": "outrospontos"}

# http://127.0.0.1:8000/randnum
@app.get("/randnum")
async def funcaoteste2():
    """Retorna uma mensagem simples de boas-vindas."""
    return {"message": True, "Numero Random": random.randint(0, 2000)}





@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    """Retorna uma mensagem simples de boas-vindas."""
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    """Retorna uma mensagem simples de boas-vindas."""
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    """Retorna uma mensagem simples de boas-vindas."""
    return id_estudante > 0

