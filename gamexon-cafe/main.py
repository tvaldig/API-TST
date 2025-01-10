import firebase_admin.auth
import uvicorn
from fastapi import FastAPI
import firebase_admin
from routers import auth_routes, cafe, game
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import pathlib
import middleware.firebase as firebase
import os
from config.db import Base, engine
basedir = pathlib.Path(__file__).parents[1]
load_dotenv(basedir / ".env")
settings = firebase.get_settings()
cred = firebase_admin.credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "./service-account.json"))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "GameXon API"}

app.include_router(cafe.router,prefix="/api/v1/cafe", tags=["Cafe"])
app.include_router(auth_routes.router,prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(game.router,prefix="/api/v1", tags=["Games"])

firebase_admin.initialize_app(cred)
print("Current App Name:", firebase_admin.get_app().project_id)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)