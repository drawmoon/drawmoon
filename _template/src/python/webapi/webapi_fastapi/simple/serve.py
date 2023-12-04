import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from loguru import logger

from .apis import router
from .exception import ParrotException


def main(
    host="0.0.0.0",
    port=8001,
    log_level: str = "INFO",
):
    logger.add(
        "parrot.log",
        format="{time} {level} {message}",
        level=log_level,
        rotation="1 MB",
        compression="zip",
    )

    app = FastAPI()
    app.include_router(router, prefix="/api")

    async def exception_handler(request: Request, call_next):
        try:
            response = await call_next(request)
        except ParrotException as e:
            logger.error(f"Exception: {e} {e.error}, {e.details}")
            response = JSONResponse(
                content={"error": e.error, "details": e.details}, status_code=400
            )
        return response

    app.middleware("http")(exception_handler)

    uvicorn.run(app, host=host, port=port, workers=1)
