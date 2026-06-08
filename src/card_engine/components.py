from pydantic import BaseModel, Field
from typing import List

class CardComponent(BaseModel):
    """A tag to identify an entity as a Card."""
    name: str = "Unknown Card"

class ZoneComponent(BaseModel):
    """A component that stores an ordered list of Card entity IDs."""
    name: str
    cards: List[str] = Field(default_factory=list)
