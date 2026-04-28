from fastapi import APIRouter, Depends
from app.utils.token import get_token
from app.service.interest_service import get_all_interest

router = APIRouter(prefix="/interest", tags=["Interest"])

@router.get("/")
async def get_by_id(
    token: str = Depends(get_token)
):
    return await get_all_interest(token)