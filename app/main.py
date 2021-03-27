import os
import json
import secrets

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.dependencies import metadata_tags

DB_DIR = os.path.join("app", "db")
DB_PATH = os.path.join(DB_DIR, "db.json")

app = FastAPI(
    title="Masterpiece Game API Server",
    description="The FastAPI version of the 60s-70s game 'Masterpiece'.",
    version="0.0.1",
    openapi_tags=metadata_tags.tags_metadata
)

def init_db():
    if not os.path.exists(DB_DIR):
        os.mkdir(DB_DIR)
    if not os.path.exists(DB_PATH):
        return {}

    with open(DB_PATH, 'r') as dbf:
        db = json.load(dbf)
        dbf.close()

    return db


DB = init_db()

@app.get("/", tags=["Health"])
def check_heartbeat():
    return {"hello there": "from Masterpiece"}