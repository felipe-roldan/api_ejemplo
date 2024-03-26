from app.suma.models.suma_request import SumaRequest
from app.suma.services.suma_service import SumaService
from fastapi import APIRouter, Response, status


router = APIRouter(
    tags=["Operations"],
)

@router.post("/api/v1/add")
async def add(input: SumaRequest, response: Response):
    response_data = {}

    try:
        suma_service = SumaService(input.num_1, input.num_2)
        response_data = {"result": suma_service.sum()}
        response.status_code = status.HTTP_200_OK
    except Exception as e:
        response_data = {"type": type(e).__name__, "message": str(e)}
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print("Exception :", e)

    return response_data