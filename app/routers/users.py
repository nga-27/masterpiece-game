from fastapi import APIRouter

from app.libs.config.users import get_users

router = APIRouter(
    prefix="/user"
)


@router.get("/", tags=["Users"])
def get_dice_roll():
    return get_users()
