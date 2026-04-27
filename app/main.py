from fastapi import APIRouter, FastAPI
# from app.routers import auth, clients

app = FastAPI(
    title="FastApi Local API",
    version="1.0.0"
)
router = APIRouter()
# app.include_router(auth.router)
# app.include_router(clients.router)


@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@router.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "API funcionando correctamente"
    }