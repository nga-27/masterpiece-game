import os
import io
import json
import secrets
import requests

from PIL import Image

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.dependencies import metadata_tags

from app.routers import dice

DB_DIR = os.path.join("app", "db")
DB_PATH = os.path.join(DB_DIR, "db.json")

RESOURCE_PATH = os.path.join(DB_DIR, "resources.json")
RESOURCE_URL = "https://raw.githubusercontent.com/nga-27/masterpiece-game-resources/main/content.json"

app = FastAPI(
    title="Masterpiece Game API Server",
    description="The FastAPI version of the 60s-70s game 'Masterpiece'.",
    version="0.0.1",
    openapi_tags=metadata_tags.tags_metadata
)

app.include_router(dice.router)


def init_db():
    if not os.path.exists(DB_DIR):
        os.mkdir(DB_DIR)
    if not os.path.exists(DB_PATH):
        return {}

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


DB = init_db()
RESOURCES = init_resources()


@app.get("/", tags=["Health"])
def check_heartbeat():
    return {"hello there": "from Masterpiece"}


@app.get("/fetch_paintings", tags=["Health"])
def fetch_paintings():
    return RESOURCES['art']


@app.get("/dl", tags=["Health"])
def download():
    # print(RESOURCES)
    painting = RESOURCES['art'][list(RESOURCES['art'].keys())[0]]
    url = os.path.join(RESOURCES['config']['base_url'], painting['filename'])
    res = requests.get(url)
    link_path = os.path.join('app', 'db', painting['filename'])
    with Image.open(io.BytesIO(res.content)) as paintf:
        paintf.save(link_path)

    return {"status": "ok"}
