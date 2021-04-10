
try:
  import unzip_requirements
except ImportError:
  pass

from fastapi import FastAPI

from app.api.routes.router import api_router
from app.core.config import (API_PREFIX, APP_NAME, APP_VERSION,
                             IS_DEBUG)
from app.core.event_handlers import (start_app_handler,
                                     stop_app_handler)
from mangum import Mangum


def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    fast_app.include_router(api_router, prefix=API_PREFIX)

    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))

    return fast_app


app = get_app()

handler = Mangum(app)
