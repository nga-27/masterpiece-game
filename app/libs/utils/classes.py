from typing import Optional
import uuid

from pydantic import BaseModel


class Painting(BaseModel):
    id: int
    title: str
    actual_value: int
    uuid: Optional[str] = uuid.uuid4()


class User(BaseModel):
    uuid: Optional[str] = uuid.uuid4()
    name: str
    character: str
    character_id: int
    current_position: int = 0
    current_roll: int = 0
    paintings: Optional[list] = []
    current_cash: int = 0


class Transaction(BaseModel):
    buyer: User
    seller: Optional[User]
    value: int
    uuid: Optional[str] = str(uuid.uuid4())
