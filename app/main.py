from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Task Service API"
)

app.include_router(router)