# Discogs Catalogue Match API

A small backend portfolio project built with Python and FastAPI to explore music catalogue search and metadata matching using the Discogs API.

The goal is to find similar or compatible releases from the user's collection. 
## What it does

The API can:

- search releases through the Discogs API;
- retrieve detailed metadata for a specific release;
- rank releases that are most similar to a selected Discogs release.

The matching logic currently compares:

- artist;
- title;
- year;
- labels;
- styles.

## Tech stack

- Python
- FastAPI
- Pydantic
- httpx
- Discogs API
- python-dotenv / pydantic-settings
- Git

## Endpoints

### Health check

```http
GET /health