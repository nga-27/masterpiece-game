import random


def roll_dice(num_dice: int = 1):
    sum_dice = 0
    for roll in range(num_dice):
        sum_dice += random.randint(1, 6)
    return sum_dice
