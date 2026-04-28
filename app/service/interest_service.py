from datetime import datetime, timezone
from fastapi import HTTPException
from app.service.http_client import client
from app.db.database import db


async def get_all_interest(token: str):
    response = await client.get(
        f"/Intereses/Listado/",
        headers={"Authorization": f"Bearer {token}"}
    )

    try:
        result = response.json()
    except Exception:
        result = {"message": response.text}

    await db.operaciones.insert_one({
        "accion": "OBTENER",
        "usuario": None,
        "cliente_id": None,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "resultado": response.status_code
    })

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=result
        )

    return {
        "status": "Success",
        "message": "Listado obtenido correctamente",
        "data": result
    }