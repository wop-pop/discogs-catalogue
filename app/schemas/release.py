from pydantic import BaseModel
from typing import Optional


class ReleaseInput(BaseModel):
    artist: str
    title: str
    year: Optional[int] = None
    label: Optional[list[str]] = []
    styles: Optional[list[str]] = []




class MatchRequest(BaseModel):
    first_release: ReleaseInput
    second_release: ReleaseInput