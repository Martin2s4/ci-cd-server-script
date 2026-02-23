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
