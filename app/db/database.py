import certifi
import ssl
from motor.motor_asyncio import AsyncIOMotorClient
from app.utils.config import DATABASE_URL, DATABASE_NAME

ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

mongo_client = AsyncIOMotorClient(
    DATABASE_URL,
    tls=True,
    tlsCAFile=certifi.where(),
    tlsAllowInvalidCertificates=True
)
db = mongo_client[DATABASE_NAME]