from fastapi import APIRouter, FastAPI
from app.routers import auth_router, client_router, interest_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastApi Local API",
    version="1.0.0",
)

#this is for test, not safe in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()
app.include_router(auth_router.router)
app.include_router(client_router.router)
app.include_router(interest_router.router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@router.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "API funcionando correctamente"
    }