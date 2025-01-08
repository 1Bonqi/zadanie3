from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def route()->dict:
    return {"message":f"Главная страница"}


@app.get("/user/admin")
async def admin()->dict:
    return {"message":f"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user(user_id:int)->dict:
    return {"message":f"Вы вошли как № {user_id}"}

@app.get("/user")
async def info(username:str, age:int)->dict:
    return {"User": username, "Age": age}