from fastapi import APIRouter
from app.suma.controller.suma_controller import router as router_suma

router = APIRouter(
    prefix="/equipo_iyc",
    tags=["Operations"],
)

router.include_router(router_suma)


