from external_service.middleware import *
from external_service.settings import *


def create_new_menu_recommendation(gender: str, mood:str, food_type:str, drink_type:str, activity_level:str):
    url = f"{settings.PARMEAMAN_URL}/api/v1/recommendation/"
    urlToken = f"{settings.PARMEAMAN_URL}/api/v1/users/login"
    payload= {
        'gender': gender,
        'mood': mood,
        'food_type': food_type,
        'drink_type': drink_type,
        'activity_level': activity_level
    }
    return POST_DATA(url, urlToken, payload)
