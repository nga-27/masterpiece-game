from fastapi import APIRouter

from app.libs.dice import roll_dice

router = APIRouter(
    prefix="/dice"
)


@router.get("/roll/{num_dice}", tags=["Dice Functions"])
def get_dice_roll(num_dice: int = 2):
    return roll_dice(num_dice)
