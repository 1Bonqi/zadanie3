from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users= {"1": 'Имя:Example, возраст:18'}

@app.get('/users')
async def get_users()->dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username:Annotated[str,Path(min_length=5,max_length=100,description='Введите свое имя',example='Vlad')]
                      ,age:Annotated[int,Path(ge=18,le=100,description='Введите свой возраст',example=24)])->str:
    user_id = str(int(max(users,key=int))+1)
    users[user_id]=f'Имя:{username},возраст:{age}'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id:Annotated[int,Path(gt=0,lt=1000,description='Введите айди',example=1)],
                       username:Annotated[str,Path(min_length=5,max_length=100,description='Измените имя',example='Egor')]
                       ,age:Annotated[int,Path(ge=18,le=100,description='Измените возраст',example=19)]) ->str:
    users[user_id]=f'Имя:{username},возраст:{age}'
    return f'The user {user_id} is update'

@app.delete('/user/{user_id}')
async def delete_user(user_id:Annotated[str,Path(description='Введите айди для удаления',example=2)])->str:
    users.pop(user_id)
    return f'User is {user_id} deleted'
    