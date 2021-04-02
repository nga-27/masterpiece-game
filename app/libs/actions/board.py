from app.libs.config.db import post_to_db, delete_from_db, patch_to_db, get_from_db


def get_users_on_board():
    board_obj = {}
    users, code = get_from_db('users', '*')
    if code != 200:
        return {"value": users}, code
    board, code = get_from_db('game_board', 'places', resources=True)
    if code != 200:
        return {"value": board}, code
    for user in users:
        board_obj[user] = {
            "position": users[user]['current_position'],
            "position_name": board[users[user]['current_position']]['title'],
            "type": board[users[user]['current_position']]['type'],
            "value": board[users[user]['current_position']]['value']
        }
    return {"value": board_obj}, 200
