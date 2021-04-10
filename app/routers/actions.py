from fastapi import APIRouter, Response, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.libs.config.actions import pop_next_painting, sell_painting_for_cash
from app.libs.utils.classes import Painting

router = APIRouter(
    prefix="/actions"
)


@router.get("/next_painting", tags=["Actions"], status_code=200)
def get_next_painting():
    return pop_next_painting()


@router.post("/sell/{name}", tags=["Actions"], status_code=201)
def sell_painting(painting: Painting, name: str):
    sold_value = sell_painting_for_cash(painting, name)
    return {"value": sold_value}, 201
