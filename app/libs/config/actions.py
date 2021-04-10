import random

from app.libs.utils.classes import Painting

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


def pop_next_painting():
    from .db import patch_to_db, get_from_db
    painting_id, code = get_from_db('painting_info', 'count')
    paintings, code = get_from_db('paintings', '*')
    next_painting = {}
    for i, title in enumerate(paintings):
        if i == painting_id:
            next_painting = paintings[title]
    _, _ = patch_to_db('painting_info', [('count', painting_id + 1)], '*')
    return {"value": next_painting}, 200


def sell_painting_for_cash(painting: Painting, name: str):
    from .db import patch_to_db, get_from_db
    player, _ = get_from_db('users', name)
    index_to_pop = 0
    for i, artwork in enumerate(player['paintings']):
        if artwork['id'] == painting.id:
            index_to_pop = i
            break
    item = player['paintings'].pop(index_to_pop)
    res, _ = patch_to_db('users', player, name)
    return item['actual_value']
