from app import main

from app.libs.config.db import post_to_db, delete_from_db
from app.libs.utils.classes import User


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


def remove_user(name):
    return delete_from_db('users', name)
