from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    M = "M"
    F = "F"

class ClientRequest(BaseModel):
    id: Optional[str] = Field(default=None)
    nombre: str
    apellidos: str
    identificacion: str

    celular: str
    otroTelefono: Optional[str] = None

    direccion: str

    fNacimiento: date
    fAfiliacion: date

    sexo: Gender

    resennaPersonal: Optional[str] = None
    imagen: Optional[str] = None

    interesFK: str

    usuarioId: str
    
class ClientListRequest(BaseModel):
    nombre: str
    usuarioId: str