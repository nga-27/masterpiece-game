from fastapi import APIRouter

from app.libs.actions.dice import roll_dice

router = APIRouter(
    prefix="/dice"
)


@router.get("/roll/{num_dice}", tags=["Dice Functions"])
def get_dice_roll(num_dice: int = 1):
    return roll_dice(num_dice)
