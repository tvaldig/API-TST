from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

api_keys = {
    "e54d4431-5dab-474e-b71a-0db1fcb9e659": "EUrRSnwrBlbAE4aLQ7iibR98EB0GkZjGMqLQwubFVRd",
}

users = {
    "EUrRSnwrBlbAE4aLQ7iibR98EB0GkZjGMqLQwubFVRd": {
        "name": "Valdi",
        "message": "Timotius Vivaldi TST",
        "email": "timtam@example.com",
        "password": pwd_context.hash("securepassword"),
    }
}

menu = [
    {"id": 1, "name": "Indomie Goreng", "price": 12000},
    {"id": 2, "name": "Toppoki", "price": 25000},
    {"id": 3, "name": "Milkis", "price": 16000},
    {"id": 4, "name": "Magelangan Rendang", "price": 50000},
    {"id": 5, "name": "Eh Teh", "price": 5000},
]

def check_api_key(api_key: str):
    return api_key in api_keys

def get_user_from_api_key(api_key: str):
    return users[api_keys[api_key]]

def get_api_key_for_user(user_id: str):
    for api_key, stored_user_id in api_keys.items():
        if stored_user_id == user_id:
            return api_key
    raise HTTPException(status_code=404, detail="API key not found")

def authenticate_user(email: str, password: str):
    for user in users.values():
        if user["email"] == email and pwd_context.verify(password, user["password"]):
            return user
    return None