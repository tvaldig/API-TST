import pickle
from typing import List
from fastapi import APIRouter, Depends, HTTPException
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from models.game import Game, GameRequest, SimilarGame
from config.db import games_collection
from middleware.authorization import JWTHandler
router = APIRouter()

data = pd.read_csv("recmodel/games_encoded.csv")

@router.get("/")
async def get_root():
    return "GAMEXON CLOUD CAFE"

def serialize_game(game):
    game["_id"] = str(game["_id"])
    return game

# GET all games
@router.get("/games", response_model=List[Game])
async def get_all_games(Authorize: JWTHandler = Depends(JWTHandler(roles=["user", "admin"]))):
    games = list(games_collection.find())
    return [serialize_game(game) for game in games]

# GET a game by ID
@router.get("/games/{game_id}", response_model=Game)
async def get_game_by_id(game_id: int, Authorize: JWTHandler = Depends(JWTHandler(roles=["user", "admin"]))):
    game = games_collection.find_one({"id": game_id})
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return serialize_game(game)

# GET a gameprice by ID
@router.get("/games/price/{game_id}")
async def get_game_by_id(game_id: int, Authorize: JWTHandler = Depends(JWTHandler(roles=["user", "admin"]))):
    game = games_collection.find_one({"id": game_id})
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"price_per_day": game["price_per_day"]}

# UPDATE game price by ID
@router.put("/games/price/{game_id}")
async def update_game_price(game_id: int, new_price: float, Authorize: JWTHandler = Depends(JWTHandler(roles=["admin"]))):
    result = games_collection.update_one({"id": game_id}, {"$set": {"price_per_day": new_price}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"message": f"Game price updated to {new_price}"}

# GAME recommendation
@router.get("/recommendations/{game_id}", response_model=List[SimilarGame])
async def get_game_recommendations(game_id:int,  Authorize: JWTHandler = Depends(JWTHandler(roles=["user", "admin"]))):
    game = games_collection.find_one({"id": game_id})
    if not game:
        raise HTTPException(status_code=404, detail="Game not found in the database")
    
    cursor = games_collection.find({}, {"_id": 0, "title": 1})
    df_game_name = pd.DataFrame(cursor)

    model = NearestNeighbors(metric='minkowski')
    data_used = data.copy()
    data_used.set_index('title', inplace=True)
    model.fit(data_used)
    distances, neighbors = model.kneighbors([data_used.iloc[game_id]], n_neighbors=4)

    similar_game = []
    for gamename in df_game_name.loc[neighbors[0][:]].values:
        similar_game.append(gamename[0])

    similar_distance = []
    for distance in distances[0]:
        similar_distance.append(f"{round(100-distance, 2)}")

    recommendations = []
    for gamename, similarity in zip(similar_game[1:], similar_distance[1:]):
        recommendations.append({
            "title": gamename,
            "similarity_score": similarity
        })

    return recommendations
   
