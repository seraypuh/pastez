from pydantic import BaseModel

class PasteCreate(BaseModel):
    title: str
    content: str

class PasteResponse(BaseModel):
    title: str
    content: str
    views: int