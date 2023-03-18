from pydantic import BaseModel


class Unit(BaseModel):
    id: int
    parent_id: int = None
    name: str
    price: int
