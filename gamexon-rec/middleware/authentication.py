from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from models.token import TokenData
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta
from models.user import UserPass
from config.db import users_collection
import os

load_dotenv(find_dotenv())
PRIVATE_KEY = os.getenv("KEY")

class AuthHandler():
    pwd = CryptContext(schemes=["bcrypt"])
    def get_password_hash(self, password):
        return self.pwd.hash(password)
    
    def get_user(self, email: str):
        user_data = users_collection.find_one({"email": email})

        if not user_data is None:
            return UserPass(**user_data)
    
    def verify_password(self, plain_password, hashed_password):
        return self.pwd.verify(plain_password, hashed_password)
    
    def authenticate_user(self, email: str, password: str):
        user = self.get_user(email)
        if not user:
            return False
        if not self.verify_password(password, user.password):
            return False
        
        return user
    
    def create_access_token(self, data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, PRIVATE_KEY)
        
        return encoded_jwt
        
    def get_current_user(self, credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]):
        credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
        try:
            payload = jwt.decode(credentials.credentials, PRIVATE_KEY)
            email: str = payload.get("sub")
            if email is None:
                raise credential_exception
            
            token_data = TokenData(email=email)    
        except JWTError:
            raise credential_exception
        
        user = self.get_user(email=token_data.email)
        if user is None:
            raise credential_exception
        
        return user


