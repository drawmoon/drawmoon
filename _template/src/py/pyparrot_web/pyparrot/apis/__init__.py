from fastapi import APIRouter

from .v1 import router as v1

router = APIRouter()
router.include_router(v1, prefix="/v1")
