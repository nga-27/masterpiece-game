import uuid

from app import main

from app.libs.config.db import post_to_db, delete_from_db, patch_to_db, get_from_db
from app.libs.utils.classes import User, NewPosition
from app.libs.actions.dice import new_roll_position


def get_users():
    return main.DB.get('users', 'none')


def add_user(user: User):
    if user.name in main.DB['users']:
        return {"value": f"Username '{user.name}' already exists."}, 409

    if user.character not in main.RESOURCES['characters']:
        list_of_ids = [main.RESOURCES['characters'][x]['id']
                       for x in main.RESOURCES['characters']]
        if user.character_id not in list_of_ids:
            return {"value": f"Character '{user.character}' not in game."}, 404
        else:
            char_index = list_of_ids.index(user.character_id)
            list_of_chars = [x for x in main.RESOURCES['characters']]
            user.character = list_of_chars[char_index]

    character_id = main.RESOURCES['characters'][user.character].get('id', 'z0')

    user_obj = User(
        name=user.name,
        character=user.character,
        character_id=character_id
    )

    item, code = post_to_db('users', user_obj, user.name)
    return {"value": item}, code


def get_characters():
    return main.RESOURCES.get('characters', {})


def map_to_user(user_obj: dict):
    new_user = User(
        name=user_obj.get('name', ''),
        uuid=user_obj.get('uuid', str(uuid.uuid4())),
        character=user_obj.get('character', ''),
        character_id=user_obj.get('character_id', 'z0'),
        current_position=user_obj.get('current_position', 0),
        current_roll=user_obj.get('current_roll', 0),
        paintings=user_obj.get('paintings', []),
        current_cash=user_obj.get('current_cash', 0)
    )
    return new_user


def remove_user(name):
    item, code = delete_from_db('users', name)
    return {"value": item}, code


#################

def user_move_piece(name: str, roll: int, direction: str):
    user, code = get_from_db('users', name)
    if code != 200:
        return {"value": user}, code
    old_position = user.get('current_position', 0)
    boolean, value = new_roll_position(roll, direction, old_position)
    if not boolean:
        return {"value": value}, 400
    user['current_position'] = value
    user['curent_roll'] = roll
    new_user = map_to_user(user)

    res, code = patch_to_db('users', new_user, name)
    return {"value": res}, code
