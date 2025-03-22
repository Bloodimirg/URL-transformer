from pydantic import BaseModel


class URL(BaseModel):
    """Model for URL"""
    url: str
