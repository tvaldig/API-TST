from fastapi import APIRouter, Depends, HTTPException, Header
from auth import get_user
from db import check_api_key, get_api_key_for_user, get_user_from_api_key, users

router = APIRouter()

@router.get("/")
async def get_users(user: dict = Depends(get_user)):
    return user

@router.get("/userid")
async def get_user_id(user: dict = Depends(get_user)):
    return {"user_id": user["name"]}

def get_user_from_header(api_key: str = Header(None)):
    """
    Dependency to retrieve a user based on the provided API key in the header.
    """
    if not api_key or not check_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return get_user_from_api_key(api_key)

@router.get("/get-api-key")
async def get_api_key(user: dict = Depends(get_user_from_header)):
    """
    Retrieve the API key for the logged-in user.
    """
    user_id = list(users.keys())[list(users.values()).index(user)]  # Find the user_id
    api_key = get_api_key_for_user(user_id)
    return {"api_key": api_key}

