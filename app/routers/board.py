from fastapi import APIRouter, Response, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.libs.actions.board import get_users_on_board


router = APIRouter(
    prefix="/board"
)


@router.get("/positions", tags=["Board"], status_code=201)
def get_users_on_board_all():
    return get_users_on_board()
