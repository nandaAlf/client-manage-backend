from datetime import datetime, timezone
from fastapi import HTTPException
from app.service.http_client import client
from app.db.database import db
from app.utils.validators.auth_validators import (
    is_valid_email,
    is_valid_password,
    validate_required_fields
)

async def login_service(username: str, password: str):

    response = await client.post(
        "/Authenticate/login/",
        data={
            "username": username,
            "password": password
        }
    )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail={
                "message": response.text
            }
        )

    result = response.json()
    await db.sesiones.insert_one({
        "token": result["token"],
        "userid": result["userid"],
        "username": username,
        "login_timestamp": datetime.utcnow().isoformat()
    })

    return {
        "status": "success",
        "data": result
    }
    


async def register_service(username: str, email: str, password: str):

    # validation
    if not validate_required_fields(username, email, password):
        raise HTTPException(
            status_code=400,
            detail="Todos los campos son obligatorios"
        )

    if not is_valid_email(email):
        raise HTTPException(
            status_code=400,
            detail="Email inválido"
        )

    if not is_valid_password(password):
        raise HTTPException(
            status_code=400,
            detail="La contraseña debe tener 8-20 caracteres, mayúscula, minúscula y número"
        )
        
    response = await client.post(
        "/Authenticate/register",
        data={
            "username": username,
            "email": email,
            "password": password
        }
    )

    try:
        result = response.json()
    except Exception:
        result = {"message": response.text}

    if response.status_code != 200:
        await db.operaciones.insert_one({
            "accion": "REGISTRO",
            "usuario": username,
            "cliente_id": None,
            "timestamp":  datetime.now(timezone.utc).isoformat(),
            "resultado": response.status_code
        })

        raise HTTPException(
            status_code=response.status_code,
            detail=result
        )

    await db.operaciones.insert_one({
        "accion": "REGISTRO",
        "usuario": username,
        "cliente_id": None,
        "timestamp":  datetime.now(timezone.utc).isoformat(),
        "resultado": 200
    })

    return {
        "status": result.get("status", "Success"),
        "message": result.get("message", "Usuario creado correctamente")
    }