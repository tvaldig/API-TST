from fastapi import APIRouter, Depends, HTTPException, Query, status
from datetime import timedelta
from middleware.authorization import JWTHandler
from models.user import User, UserLogin, UserPass
from models.token import Token
from middleware.authentication import AuthHandler
from config.db import users_collection

router = APIRouter()
auth = AuthHandler()

@router.post("/login", response_model=Token)
async def login(form_data: UserLogin):
    user = auth.authenticate_user(form_data.email, form_data.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password", headers={"WWW-Authenticate": "Bearer"})
    
    access_token_expires = timedelta(minutes=15)
    access_token = auth.create_access_token(data={"sub":user.email}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model= User)
async def read_users_me(current_user: User = Depends(JWTHandler())):
    return current_user

@router.post("/register", response_model=Token)
async def register(user: UserPass):
    # Check if the user already exists
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    user_dict = UserPass(
        username=user.username,
        email=user.email,
        password=auth.get_password_hash(user.password),
        role=user.role
    )


    insert_result = users_collection.insert_one(dict(user_dict))
    print("Insert Result ID:", insert_result.inserted_id)


    inserted_user = users_collection.find_one({"_id": insert_result.inserted_id})
    print("Inserted User:", inserted_user)

    access_token_expires = timedelta(minutes=15)
    access_token = auth.create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
