import os

from fastapi import APIRouter

api = APIRouter(prefix="/parrots", tags=["parrots"])


@api.get("/")
def fetch() -> list[str]:
    return ["Hello", os.getenv("PYPARROT")]
