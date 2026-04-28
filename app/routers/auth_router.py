from fastapi import APIRouter, Depends
from app.models.auth import AuthRequest, RegisterRequest
from app.service.auth_service import login_service, logout_service, register_service
from app.utils.token import get_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login/")
async def login(data: AuthRequest):
    return await login_service(data.username, data.password)

@router.post("/register/")
async def login(data: RegisterRequest):
    return await register_service(data.username, data.email, data.password)

@router.post("/logout/")
async def logout(token: str = Depends(get_token)):
    return await logout_service(token)