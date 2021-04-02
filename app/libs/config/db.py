import os
import json
import requests
import pprint
import uuid

from app import main
from app.libs.utils.classes import (
    User, Painting, Transaction
)
from .painting_utils import set_painting_values

DB_DIR = os.path.join("app", "db")
DB_PATH = os.path.join(DB_DIR, "db.json")

RESOURCE_PATH = os.path.join(DB_DIR, "resources.json")
RESOURCE_URL = "https://raw.githubusercontent.com/nga-27/masterpiece-game-resources/main/content.json"


def init_db_tables():
    db = {}
    db['users'] = {}
    db['transactions'] = []
    db['paintings'] = {}
    with open(DB_PATH, 'w') as dbf:
        json.dump(db, dbf)
        dbf.close()
    return db


def init_db():
    if not os.path.exists(DB_DIR):
        os.mkdir(DB_DIR)
    if not os.path.exists(DB_PATH):
        return init_db_tables()

    with open(DB_PATH, 'r') as dbf:
        db = json.load(dbf)
        dbf.close()

    return db


def init_resources():
    if not os.path.exists(DB_DIR):
        os.mkdir(DB_DIR)
    if os.path.exists(RESOURCE_PATH):
        os.remove(RESOURCE_PATH)

    res = requests.get(RESOURCE_URL)
    with open(RESOURCE_PATH, 'wb') as res_file:
        res_file.write(res.content)
        res_file.close()

    with open(RESOURCE_PATH, 'r') as resf:
        db = json.load(resf)
        resf.close()

    base_url = db['config']['base_url']
    for painting in db['art']:
        db['art'][painting]['url'] = os.path.join(
            base_url, db['art'][painting]['filename'])

    return db

##############################################


def update_db(db_obj):
    with open(DB_PATH, 'w') as dbf:
        json.dump(db_obj, dbf)
        dbf.close()
    return


def read_db():
    db = {}
    if os.path.exists(DB_PATH):
        with open(DB_PATH, 'r') as dbf:
            db = json.load(dbf)
            dbf.close()
    return db


def stringify_for_json(item):
    if not isinstance(item, (str, int, list)):
        item = str(item)
        item.replace("'", '"')
    return item

##############################################


def post_to_db(table: str, object_to_post, store_key, patch=False):
    if stringify_for_json(store_key) in main.DB[table] and not patch:
        return "Record already exists", 409

    store_key = stringify_for_json(store_key)
    main.DB[table][store_key] = {}
    for item in object_to_post:
        main.DB[table][store_key][stringify_for_json(
            item[0])] = stringify_for_json(item[1])

    update_db(main.DB)
    return main.DB[table][store_key], 201


def delete_from_db(table: str, store_key):
    if stringify_for_json(store_key) not in main.DB[table]:
        return "Record not found", 404

    store_key = stringify_for_json(store_key)
    try:
        main.DB[table].pop(store_key)
        update_db(main.DB)
    except:
        return f"Error in deleting {store_key}", 500
    return "Success", 201


def get_from_db(table: str, store_key):
    if stringify_for_json(store_key) not in main.DB[table]:
        return "Record not found", 404
    return main.DB[table][store_key], 200


def patch_to_db(table: str, object_to_patch, store_key):
    if stringify_for_json(store_key) not in main.DB[table]:
        return "Record not found", 404
    return post_to_db(table, object_to_patch, store_key, patch=True)

##############################################


def load_db(db, resources):
    value_list = set_painting_values(len(resources['art']))
    for i, paint_title in enumerate(resources['art']):
        new_painting = Painting(
            id=i,
            title=paint_title,
            actual_value=value_list[i],
            uuid=str(uuid.uuid4())
        )
        post_to_db('paintings', new_painting, new_painting.title)
    return


##############################################


def fetch_paintings_from_db():
    return main.RESOURCES['art']
