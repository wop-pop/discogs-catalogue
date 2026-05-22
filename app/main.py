from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Discogs Match API",
    description="A small FastAPI backend for searching Discogs releases and comparing music metadata.",
    version="0.1.0",
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}