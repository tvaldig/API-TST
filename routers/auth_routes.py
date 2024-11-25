from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from db import authenticate_user, users, pwd_context

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("/login")
async def login(request: LoginRequest):
    user = authenticate_user(request.email, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user": user}

@router.post("/register")
async def register(request: RegisterRequest):
    if request.email in [u["email"] for u in users.values()]:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = {
        "name": request.name,
        "email": request.email,
        "password": pwd_context.hash(request.password),
    }
    users[request.email] = new_user
    return {"message": "User registered successfully", "user": new_user}