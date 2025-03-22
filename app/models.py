from pydantic import BaseModel


class URLRequest(BaseModel):
    """Model for URL request"""
    url: str
