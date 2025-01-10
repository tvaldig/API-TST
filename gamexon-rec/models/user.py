from pydantic import BaseModel
from typing import Literal
from datetime import date

class User(BaseModel):
    username: str
    email: str
    role: Literal ["user", "admin"]

class UserPass(User):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str