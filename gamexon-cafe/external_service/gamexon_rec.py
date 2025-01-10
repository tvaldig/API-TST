from external_service.middleware import *
from external_service.settings import *

def get_games():
    url = f"{settings.GAMEXONREC_URL}/api/v1/public/games"
    urlToken = f"{settings.GAMEXONREC_URL}/api/v1/auth/login"
    return GET_DATA(url, urlToken)

def get_game_by_id(id: int):
    url = f"{settings.GAMEXONREC_URL}/api/v1/public/games/{id}"
    urlToken = f"{settings.GAMEXONREC_URL}/api/v1/auth/login"
    return GET_DATA(url, urlToken)

def get_gameprice_by_id(id: int):
    url = f"{settings.GAMEXONREC_URL}/api/v1/public/games/price/{id}"
    urlToken = f"{settings.GAMEXONREC_URL}/api/v1/auth/login"
    return GET_DATA(url, urlToken)

def create_game_recommendation(id: int):
    url = f"{settings.GAMEXONREC_URL}/api/v1/public/recommendations/{id}"
    urlToken = f"{settings.GAMEXONREC_URL}/api/v1/auth/login"
    return GET_DATA(url, urlToken)
