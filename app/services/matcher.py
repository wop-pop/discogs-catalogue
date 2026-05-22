from difflib import SequenceMatcher


def similarity(a: str, b: str) -> float:
    return round(SequenceMatcher(None, a.lower(), b.lower()).ratio(), 2)


def compare_releases(first: dict, second: dict):
    artist_score = similarity(
        first.get("artist", ""),
        second.get("artist", ""),
    )

    title_score = similarity(
        first.get("title", ""),
        second.get("title", ""),
    )


    delta = abs(int(first.get("year")) - int(second.get("year")))
    year_score = 1 - 0.01 * delta 

    overall_score = round(
        artist_score * 0.4 + title_score * 0.4 + year_score * 0.2,
        2,
    )

    return {
        "artist_score": artist_score,
        "title_score": title_score,
        "year_score": year_score,
        "overall_score": overall_score,
        "match": overall_score >= 0.75,
    }