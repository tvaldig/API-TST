from fastapi import APIRouter, HTTPException
from external_service.gamexon_rec import get_games, get_game_by_id, get_gameprice_by_id, create_game_recommendation

router = APIRouter()

# GET all games
@router.get("/games")
async def get_all_games():
    try:
        return get_games()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET a game by ID
@router.get("/games/{game_id}")
async def get_game_by_id_route(game_id: int):
    try:
        return get_game_by_id(game_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# GET a game price by ID
@router.get("/games/price/{game_id}")
async def get_game_price_by_id(game_id: int):
    try:
        return get_gameprice_by_id(game_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# POST create game recommendation
@router.get("/recommendations/{game_id}")
async def create_game_recommendations(game_id:int):
    try:
        recommendations = create_game_recommendation(game_id)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
