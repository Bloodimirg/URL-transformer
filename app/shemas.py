from pydantic import BaseModel


class URLRequest(BaseModel):
    """scheme for transmitting a request between a client and a server"""
    url: str


class URLResponse(BaseModel):
    """Schemes for transmitting a short URL response"""
    shortened_url_id: str
