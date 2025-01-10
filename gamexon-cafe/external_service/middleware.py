import requests
from external_service.settings import settings

def get_token(url: str):
    if url == f"{settings.GAMEXONREC_URL}/api/v1/auth/login":
        data = {
            'email': settings.GAMEXONREC_USERNAME,
            'password': settings.GAMEXONREC_PASSWORD
        }
        response = requests.post(url, json=data)
    elif url == f"{settings.PARMEAMAN_URL}/api/v1/users/login":
        data = {
            'email': settings.PARMEAMAN_USERNAME,
            'password': settings.PARMEAMAN_PASSWORD
        }
        response = requests.post(url, json=data)
    return response.json()["access_token"]

def GET_DATA(url: str, urlToken: str):
    headers = {
        'Authorization': f'Bearer {get_token(urlToken)}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def POST_DATA(url, urlToken, payload):
    headers = {
        'Authorization': f'Bearer {get_token(urlToken)}'
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def PUT_DATA(url, urlToken, payload):
    headers = {
        'Authorization': f'Bearer {get_token(urlToken)}'
    }
    response = requests.put(url, headers=headers, json=payload)
    return response.json()

def DELETE_DATA(url, urlToken):
    headers = {
        'Authorization': f'Bearer {get_token(urlToken)}'
    }
    response = requests.delete(url, headers=headers)
    return response.json()