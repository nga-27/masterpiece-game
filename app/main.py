import os
import io
import json
import secrets
import requests

from PIL import Image

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.dependencies import metadata_tags

from app.routers import dice, users
from app.libs.config.db import init_db, DB_DIR, fetch_paintings_from_db

app = FastAPI(
    title="Masterpiece Game API Server",
    description="The FastAPI version of the 60s-70s game 'Masterpiece'.",
    version="0.0.1",
    openapi_tags=metadata_tags.tags_metadata
)

app.include_router(dice.router)
app.include_router(users.router)


@app.get("/", tags=["Health"])
def check_heartbeat():
    return {"hello there": "from Masterpiece"}


@app.get("/fetch_paintings", tags=["Health"])
def fetch_paintings():
    return fetch_paintings_from_db()


# @app.get("/dl", tags=["Health"])
# def download():
#     # print(RESOURCES)
#     painting = RESOURCES['art'][list(RESOURCES['art'].keys())[0]]
#     url = os.path.join(RESOURCES['config']['base_url'], painting['filename'])
#     res = requests.get(url)
#     link_path = os.path.join('app', 'db', painting['filename'])
#     with Image.open(io.BytesIO(res.content)) as paintf:
#         paintf.save(link_path)

#     return {"status": "ok"}
