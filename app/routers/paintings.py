from fastapi import APIRouter, Response, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.libs.config.painting_utils import pop_next_painting

router = APIRouter(
    prefix="/paintings"
)


@router.get("/next", tags=["Paintings"], status_code=200)
def get_next_painting():
    return pop_next_painting()
