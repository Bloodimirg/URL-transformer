from fastapi import FastAPI
from app.urls import router

app = FastAPI()

# connection router
app.include_router(router)
