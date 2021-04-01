from app import main


def get_users():
    return main.DB.get('users', 'none')
