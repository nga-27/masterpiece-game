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
    character_id: Optional[str] = 'z0'
    current_position: Optional[int] = 0
    current_roll: Optional[int] = 0
    paintings: Optional[list] = []
    current_cash: Optional[int] = 1500000


class Transaction(BaseModel):
    buyer: User
    seller: Optional[User]
    value: int
    uuid: Optional[str] = str(uuid.uuid4())


class NewPosition(BaseModel):
    name: str
    roll_value: int
    move_direction: str
    position: int
