import uvicorn
from fastapi import FastAPI
from routers import auth_routes, game
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "GameXon Game-Recommendation API"}

app.include_router(game.router,prefix="/api/v1/public")
app.include_router(auth_routes.router,prefix="/api/v1/auth")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)