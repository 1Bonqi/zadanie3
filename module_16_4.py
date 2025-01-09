from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()
users = []
class User(BaseModel):
    id:int=None
    username:str
    age:int

@app.get('/users')
async def get_users()->list[User]:
    return users

@app.post('/user/{username}/{age}')
async def create_user(user:User,username:Annotated[str,Path(min_length=5,max_length=100,description='Введите свое имя',example='Vlad')]
                      ,age:Annotated[int,Path(ge=18,le=100,description='Введите свой возраст',example=24)])->str:
    if users:
        user_id=max(user.id for user in users)+1
    else:
        user_id=1

    user = User(id=user_id,username=username,age=age)
    users.append(user)
    return f'User {user} is registret'

@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id:Annotated[int,Path(gt=0,lt=1000,description='Введите айди',example=1)],
                       username:Annotated[str,Path(min_length=5,max_length=100,description='Измените имя',example='Egor')]
                       ,age:Annotated[int,Path(ge=18,le=100,description='Измените возраст',example=19)]) ->str:
    try:
        user = User(id=user_id,username=username,age=age)
        return f'The user {user_id} is update:{user}'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id:Annotated[int,Path(description='Введите айди для удаления',example=2)])->str:
    try:
        users.pop(user_id)
        return f'User is {user_id} deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


