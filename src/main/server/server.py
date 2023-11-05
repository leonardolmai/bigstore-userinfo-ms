from fastapi import FastAPI

from src.presentation.routers import card_router

app = FastAPI()

app.include_router(card_router.router)
