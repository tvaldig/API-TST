from pydantic import BaseModel
from datetime import date

class Game(BaseModel):
    id: int
    title: str
    genre: str
    release_year: int
    popularity: float
    developer: str
    publisher: str
    price_per_day: float 
    rating: str

class GameRequest(BaseModel):
    id: int

class SimilarGame(BaseModel):
    title: str
    similarity_score: float
