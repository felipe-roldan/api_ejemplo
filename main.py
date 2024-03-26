from fastapi import FastAPI
from app.routers.health import router as router_health
from app.routers.api import router as router_api

main = FastAPI()
main.include_router(router_health)
main.include_router(router_api)