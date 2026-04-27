import httpx
from app.utils.config import BASE_URL

class HttpClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.client = httpx.AsyncClient(
            timeout=30.0
        )

    async def post(self, url: str, data=None, headers=None):
        return await self.client.post(
            self.base_url + url,
            json=data,
            headers=headers
        )

    async def get(self, url: str, headers=None):
        return await self.client.get(
            self.base_url + url,
            headers=headers
        )

    async def patch(self, url: str, data=None, headers=None):
        return await self.client.patch(
            self.base_url + url,
            json=data,
            headers=headers
        )

    async def delete(self, url: str, headers=None):
        return await self.client.delete(
            self.base_url + url,
            headers=headers
        )

    async def close(self):
        await self.client.aclose()


client = HttpClient()