import random

VALUES = [
    1000000,
    750000,
    700000,
    650000,
    600000,
    550000,
    500000,
    450000,
    400000,
    350000,
    300000,
    250000,
    200000,
    150000,
    100000,
    0
]


def set_painting_values(num_values=24):
    new_list = VALUES.copy()

    # Add [at least] one more forgery
    needed_items = num_values - len(new_list) - 1
    new_list.append(0)

    rand_indexes = [random.randint(0, 15) for _ in range(needed_items)]
    for rand_index in rand_indexes:
        new_list.append(VALUES[rand_index])
    shuffled_list = shuffle_list(new_list)
    return shuffled_list


def shuffle_list(ordered_list: list):
    shuffled = []
    while len(ordered_list) > 0:
        index = random.randint(0, len(ordered_list)-1)
        shuffled.append(ordered_list.pop(index))

    return shuffled
