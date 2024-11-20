#predefined API key for testing
api_keys = {
    "e54d4431-5dab-474e-b71a-0db1fcb9e659": "7oDYjo3d9r58EJKYi5x4E8",
}

users = {
    "7oDYjo3d9r58EJKYi5x4E8": {
        "name" : "Valdi",
        "message": "Timotius Vivaldi Gunawan 18222091"
    },
}

def check_api_key(api_key: str):
    return api_key in api_keys

def get_user_from_api_key(api_key: str):
    return users[api_keys[api_key]]