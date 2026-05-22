import httpx
from fastapi import HTTPException
from app.config import settings

BASE_URL = "https://api.discogs.com"


async def search_releases(query: str):
    headers = {
        "Authorization": f"Discogs token={settings.discogs_user_token}",
        "User-Agent": "discogs-match-api/0.1",
    }

    params = {
        "q": query,
        "type": "release",
        "per_page": 10,
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            f"{BASE_URL}/database/search",
            headers=headers,
            params=params,
        )

    if response.status_code == 401:
        raise HTTPException(status_code=401, detail="Invalid Discogs token")

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Discogs API error",
        )

    return response.json()


async def get_release(release_id: int):
    headers = {
        "Authorization": f"Discogs token={settings.discogs_user_token}",
        "User-Agent": "discogs-match-api/0.1",
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            f"{BASE_URL}/releases/{release_id}",
            headers=headers,
        )

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Release not found")

    if response.status_code == 401:
        raise HTTPException(status_code=401, detail="Invalid Discogs token")

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Discogs API error",
        )

    return response.json()