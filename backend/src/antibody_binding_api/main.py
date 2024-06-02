from fastapi import FastAPI
from .routes.endpoints import router as api_router

from ._version import __version__

api = FastAPI(version=__version__)

api.include_router(api_router)

app = FastAPI()

app.mount("/api", api)