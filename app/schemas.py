from pydantic import BaseModel
from typing import List

class FlashcardItem(BaseModel):
    quetion: str
    answer: str

class FlashcardRequest(BaseModel):
    text: str

class FlashcardResponse(BaseModel):
    cards: List[FlashcardItem]
    