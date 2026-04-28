from fastapi import APIRouter, Depends, Request
from app.models.client import ClientListRequest, ClientRequest
from app.service.client_service import create_client, get_client_by_id, update_client, get_all_clients
from app.utils.token import get_token

router = APIRouter(prefix="/client", tags=["Client"])

@router.post("/list/")
async def getAll(data: ClientListRequest, token: str = Depends(get_token)):
    return await get_all_clients(data, token)

@router.get("/{cliente_id}")
async def get_by_id(
    cliente_id: str,
    token: str = Depends(get_token)
):
    return await get_client_by_id(cliente_id, token)

@router.post("/")
async def create(data: ClientRequest, token: str = Depends(get_token)):
    return await create_client(data, token)
    return await create_client(data, token)

@router.patch("/")
async def update(request: Request, data: ClientRequest,token: str = Depends(get_token)):
    raw = await request.body()
    return await update_client(data, token)
