from fastapi import APIRouter
from app.models.auth import AuthRequest, RegisterRequest
from app.service.auth_service import login_service, register_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login(data: AuthRequest):
    return await login_service(data.username, data.password)

@router.post("/register")
async def login(data: RegisterRequest):
    return await register_service(data.username, data.email, data.password)