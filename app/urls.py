from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from app.models import URL
from app.services import add_url_to_db, get_original_url_from_db
import httpx

router = APIRouter()


@router.get("/")
async def root():
    return FileResponse("public/index.html")


@router.post("/", status_code=201)
async def create_shortened_url(request: URL):
    original_url = request.url
    shortened_id = add_url_to_db(original_url)
    return {"shortened_url_id": shortened_id}


@router.get("/{shortened_id}")
async def get_original_url(shortened_id: str):
    original_url = get_original_url_from_db(shortened_id)
    if original_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=original_url, status_code=307)


async def fetch_data_from_service(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@router.get("/async-request")
async def async_service_request(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="URL parameter is required for async request")
    try:
        data = await fetch_data_from_service(url)
        return data
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=str(e))
