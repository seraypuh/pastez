from sqlalchemy import Column, Integer, String, Text, Boolean
from .database import Base


class Paste(Base):
    __tablename__ = "pastes"

    id = Column(Integer, primary_key=True)
    slug = Column(String, unique=True)
    title = Column(String)
    content = Column(Text)
    views = Column(Integer, default=0)

