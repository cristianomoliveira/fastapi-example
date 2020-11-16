from datetime import datetime, time, date
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, Response, UJSONResponse
#from app.core.config import settings



app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'])



class User(BaseModel):
    id: Optional[int] = 0
    usuario: str
    email: str
    data_de_inclusao: Optional[date]
    data_de_alteracao: Optional[date]
    regras: Optional[str] = None
    status: Optional[str] = None
    acoes: Optional[str] = None 


fake_users_db = [
    User(id=1, usuario='ANPINA', email='antonio.pina@tvglobo.com.br', data_de_inclusao='2019-05-28', data_de_alteracao='2019-05-30', regras='01', status='ATIVO'),
    User(id=2, usuario='CCHANG', email='ciro.chang@tvglobo.com.br', data_de_inclusao='2019-05-28', data_de_alteracao='2019-05-30', regras='01', status='ATIVO'),
    User(id=3, usuario='TMARCAL', email='thiago.marcal@tvglobo.com.br', data_de_inclusao='2019-05-28', data_de_alteracao='2019-05-30', regras='01', status='ATIVO'),
    User(id=4, usuario='ECGIANN', email='ecgiannotto@tvglobo.com.br', data_de_inclusao='2019-05-28', data_de_alteracao='2019-05-30', regras='01', status='ATIVO'),
    User(id=5, usuario='YFERNAND', email='yturi.vasquez@tvglobo.com.br', data_de_inclusao='2019-05-28', data_de_alteracao='2019-05-30', regras='02', status='ATIVO'),
    User(id=5, usuario='PLACERDA', email='pedro.soares.lacerda@tvglobo.com.br', data_de_inclusao='2019-05-28', data_de_alteracao='2019-05-30', regras='02', status='ATIVO'),
]


@app.get('/')
async def root():
    return {'message': 'A API está rodando ...'}

@app.get('/usuarios/{user_id}')
def read(user_id: int):
    """Rota que retorna um usuário"""
    return {'user': [user for user in fake_users_db if user.id == user_id]}

@app.get('/usuarios/')
async def read_pagination(skip: int = 0, limit: int = 10):
    """Rota para listar todos os usuários"""
    return {'users': fake_users_db[skip: skip + limit]}

@app.post('/usuarios')
def create_user(user: User):
    """Rota para criar usuários"""
    user.id = fake_users_db[-1].id + 1
    fake_users_db.append(user)
    return {'message': 'Usuário foi criado com sucesso'}

@app.patch('/usuarios/{user_id}')
def update(user_id: int, user: User):
    """Rota para atualizar um usuário"""
    index = [index for index, user in enumerate(fake_users_db) if user.id == user_id]
    user.id = fake_users_db[index[0]].id
    fake_users_db[index[0]] = user
    return {'message': 'Usuário atualizado com sucesso'}

@app.delete('/usuarios/{user_id}')
def delete(user_id: int):
    """Rota para apagar um usuário"""
    user = [user for user in fake_users_db if user.id == user_id]
    fake_users_db.remove(user[0])
    return {'message': 'Usuário foi removido com sucesso'}