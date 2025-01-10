import os
import pathlib
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import Annotated, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin.auth import verify_id_token
import pyrebase

basedir = pathlib.Path(__file__).parents[1]
load_dotenv(basedir / ".env")
bearer_scheme = HTTPBearer(auto_error=False)

class Settings(BaseSettings):
    app_name: str = "demofirebase"
    env: str = os.getenv("ENV", "development")
    frontend_url: str = os.getenv("FRONTEND_URL", "NA")

@lru_cache
def get_settings() -> Settings:
    return Settings()

def get_firebase_config():
    firebaseConfig = {
  "apiKey": "AIzaSyBks4TIJuDOn2DhIieA9aqNFOYvGhSsjCc",
  "authDomain": "tst-gamexon.firebaseapp.com",
  "projectId": "tst-gamexon",
  "storageBucket": "tst-gamexon.firebasestorage.app",
  "databaseURL" : "",
  "messagingSenderId": "141632866319",
  "appId": "1:141632866319:web:79e2c82d10eb39f227fb7a",
  "measurementId": "G-K4V5CLN5ZX"
    }

    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase

def get_firebase_user_from_token(
    token: Annotated[Optional[HTTPAuthorizationCredentials], Depends(bearer_scheme)],
) -> dict:
    try:
        if not token:
            raise ValueError("No token")

        decoded_token = verify_id_token(token.credentials)

        role = decoded_token.get("role", "user") 
        decoded_token["role"] = role
        return decoded_token
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

def check_admin_role(user: dict):
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions"
        )
