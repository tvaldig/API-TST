from fastapi import APIRouter
from db import menu
router = APIRouter()

@router.get("/")
async def get_testroute():
    return "PUBLIC ROUTE"

@router.get("/menu")
async def get_menu():
 
    return {"menu": menu}