from fastapi import FastAPI,Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def route()->dict:
    return {"message":f"Главная страница"}


@app.get("/user/admin")
async def admin()->dict:
    return {"message":f"Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user(user_id:int=Path(ge=1,le=100,description='Enter User ID',example=15))->dict:
    return {"message":f"Вы вошли как № {user_id}"}

@app.get("/user/{username}/{age}")
async def info(username:str=Path(min_length=5,max_length=20,description='Enter username',example='vlad')
               , age:int=Path(ge=18,le=120,description='Enter age',example=24))->dict:
    return {'message':f'{username} {age}'}