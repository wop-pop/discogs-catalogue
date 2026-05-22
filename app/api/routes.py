from fastapi import APIRouter, Query
from app.services.discogs_client import search_releases, get_release
from app.services.matcher import compare_releases
from app.schemas.release import MatchRequest

router = APIRouter()


@router.get("/search")
async def search(query: str = Query(..., min_length=2)):
    data = await search_releases(query)

    results = []

    for item in data.get("results", []):
        results.append(
            {
                "id": item.get("id"),
                "title": item.get("title"),
                "year": item.get("year"),
                "country": item.get("country"),
                "format": item.get("format"),
                "thumb": item.get("thumb"),
            }
        )

    return {
        "query": query,
        "results_count": len(results),
        "results": results,
    }


@router.get("/releases/{release_id}")
async def release_detail(release_id: int):
    data = await get_release(release_id)

    return {
        "id": data.get("id"),
        "title": data.get("title"),
        "year": data.get("year"),
        "country": data.get("country"),
        "genres": data.get("genres"),
        "styles": data.get("styles"),
        "labels": data.get("labels"),
        "artists": data.get("artists"),
        "tracklist": data.get("tracklist"),
    }


@router.post("/match")
async def match_releases(payload: MatchRequest):
    return compare_releases(
        payload.first_release.model_dump(),
        payload.second_release.model_dump(),
    )