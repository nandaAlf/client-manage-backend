from datetime import datetime, timezone
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.service.http_client import client
from app.db.database import db


async def get_all_clients(data, token: str):
    payload = jsonable_encoder(data)

    response = await client.post(
        "/Cliente/Listado/",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    try:
        result = response.json()
    except Exception:
        result = {"message": response.text}

    await db.operaciones.insert_one({
        "accion": "LISTAR",
        "usuario": data.usuarioId,
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
        "status":  "Success",
        "message": "Listado de clientes obtenido correctamente",
        "data": result
    }

async def get_client_by_id(cliente_id: str, token: str):
    response = await client.get(
        f"/Cliente/Obtener/{cliente_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    try:
        result = response.json()
    except Exception:
        result = {"message": response.text}

    await db.operaciones.insert_one({
        "accion": "OBTENER",
        "usuario": None,
        "cliente_id": cliente_id,
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
        "message": "Cliente obtenido correctamente",
        "data": result
    }

async def create_client(data, token: str):

    payload = jsonable_encoder(data)
    payload["fNacimiento"] = data.fNacimiento.isoformat()
    payload["fAfiliacion"] = data.fAfiliacion.isoformat()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = await client.post("/Cliente/Crear", data=payload, headers=headers)

    try:
        result = response.json()
    except Exception:
        result = {"message": response.text}

    if response.status_code != 200:
        await db.operaciones.insert_one({
            "accion": "CREAR",
            "usuario": data.usuarioId,
            "cliente_id": None,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "resultado": response.status_code
        })

        raise HTTPException(
            status_code=response.status_code,
            detail=result
        )

    cliente_id = result.get("id") or result.get("clienteId")

    await db.operaciones.insert_one({
        "accion": "CREAR",
        "usuario": data.usuarioId,
        "cliente_id": cliente_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "resultado": 200
    })

    return {
        "status": result.get("status", "Success"),
        "message": result.get("message") or "Cliente creado correctamente",
        "data": result
    }
    
    
async def update_client(data, token: str):

    payload = jsonable_encoder(data)
    if (data.fNacimiento):
        payload["fNacimiento"] = data.fNacimiento.isoformat()
    if(data.fAfiliacion):    
        payload["fAfiliacion"] = data.fAfiliacion.isoformat()

    response = await client.post(
        "/Cliente/Actualizar/",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    
    try:
        result = response.json()
    except Exception:
        result = {"message": response.text}
    
    await db.operaciones.insert_one({
        "accion": "ACTUALIZAR",
        "usuario": data.usuarioId,
        "cliente_id": data.identificacion,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "resultado": response.status_code
    })

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=result
        )

    return {
        "status": result.get("status", "Success"),
        "message": result.get("message") or "Cliente actualizado correctamente",
        "data": result
    }
    
