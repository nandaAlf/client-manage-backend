# client-manage-backend

API intermedia construida con **FastAPI** que actúa como capa entre el frontend y la API oficial de gestión de clientes. Registra operaciones en **MongoDB** y gestiona autenticación mediante JWT.

---

## Tecnologías

- Python 3.11
- FastAPI
- Motor (MongoDB async)
- httpx
- MongoDB Atlas (producción) / MongoDB Docker (local)
- Docker & Docker Compose

---

## Estructura del proyecto

```
app/
├── main.py                  # Entrada de la aplicación
├── db/
│   └── database.py          # Conexión a MongoDB con Motor
├── models/
│   ├── auth.py              # Modelos de autenticación
│   └── client.py            # Modelos de cliente
├── routers/
│   ├── auth_router.py       # Rutas de autenticación
│   ├── client_router.py     # Rutas de clientes
│   └── interest_router.py   # Rutas de intereses
├── service/
│   ├── auth_service.py      # Lógica de autenticación
│   ├── client_service.py    # Lógica de clientes
│   ├── interest_service.py  # Lógica de intereses
│   └── http_client.py       # Cliente HTTP hacia la API oficial
└── utils/
    ├── config.py             # Variables de entorno
    ├── token.py              # Extracción y validación del token
    └── validators/
        └── auth_validators.py
```

---

## Endpoints

### Auth — `/auth`

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/auth/login/` | Inicia sesión y guarda la sesión en MongoDB |
| POST | `/auth/register/` | Registra un nuevo usuario |
| POST | `/auth/logout/` | Cierra sesión y elimina el documento de sesión |

### Clientes — `/client`

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/client/list` | Lista clientes filtrados por nombre |
| GET | `/client/{cliente_id}` | Obtiene un cliente por ID |
| POST | `/client/` | Crea un nuevo cliente |
| PATCH | `/client/` | Actualiza un cliente existente |

### Intereses — `/interest`

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/interest/` | Lista todos los intereses disponibles |

---

## Variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```dotenv
BASE_URL=https://pruebareactjs.test-class.com/Api/api
DATABASE_NAME=client_manage
DATABASE_URL=mongodb://admin:admin123@localhost:27017
```

Para producción, configura en el dashboard:

```dotenv
BASE_URL=https://pruebareactjs.test-class.com/Api/api
DATABASE_NAME=client_manage
DATABASE_URL=mongodb+srv://<user>:<password>@cluster0.mongodb.net/client_manage?retryWrites=true&w=majority&appName=Cluster0
```

---

## Desarrollo local

### Requisitos
- Docker y Docker Compose
- Python 3.11+

### Con Docker Compose

```bash
docker-compose up --build
```

Esto levanta la API en `http://localhost:8000` y MongoDB en `localhost:27017`.

### Sin Docker

```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## Documentación interactiva

Una vez levantada la app:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---


## MongoDB — Colecciones

| Colección | Descripción |
|-----------|-------------|
| `sesiones` | Documentos de sesiones activas (se eliminan al hacer logout) |
| `operaciones` | Registro de acciones realizadas (crear, actualizar, listar, obtener) |