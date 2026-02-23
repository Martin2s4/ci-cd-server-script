from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []
class User(BaseModel):
    id: int
    name:str


@app.get("/")
def home():
    return {"message": "Backend is running"}

def get_users():
    return users

@app.post("/users")
def create_user(user: User):
    user.append(user)
    return {"message": "user created successfully", "user": user}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
        return {"message": "user not found" }
    

@app.get("/search")
def search_users(name: str):
    results = [user for user in users if name.lower() in user.name.lower()]
    return results