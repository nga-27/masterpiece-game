import random

ROLL_DIRECTIONS = ['cw', 'ccw']
MAX_POSITION = 30


def roll_dice(num_dice: int = 1):
    sum_dice = 0
    for roll in range(num_dice):
        sum_dice += random.randint(1, 6)
    return sum_dice


def roll_validation(roll_val: int):
    if roll_val < 1 or roll_val > 6:
        return False
    return True


def new_roll_position(roll_val: int, direction: str, old_position: int):
    if not roll_validation(roll_val):
        return False, f"Bad roll {roll_val}"
    if direction not in ROLL_DIRECTIONS:
        return False, f"Invalid direction {direction}"

    if direction == 'cw':
        new_position = (old_position + roll_val) % MAX_POSITION
    else:
        new_position = old_position - roll_val
        if new_position < 0:
            new_position = MAX_POSITION + new_position
    return True, new_position
