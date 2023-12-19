from fastapi import FastAPI

from src.presentation.routers import address_router

app = FastAPI()

app.include_router(address_router.router)
