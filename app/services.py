import hashlib

# storage short URL
url_db = {}


# Function for generate short URL
def shorten_url(original_url: str) -> str:
    # Use the first 6 characters of the hashed value
    return hashlib.md5(original_url.encode()).hexdigest()[:6]


def add_url_to_db(original_url: str) -> str:
    shortened_id = shorten_url(original_url)
    url_db[shortened_id] = original_url
    return shortened_id


def get_original_url_from_db(shortened_id: str) -> str:
    """Get original URL"""
    return url_db.get(shortened_id)
