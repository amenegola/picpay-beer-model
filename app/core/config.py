from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "0.0.1"
APP_NAME = "Beer Model IBU Prediction"
API_PREFIX = "/api"

config = Config(".env")

IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

API_KEY: Secret = config("API_KEY", cast=Secret)

BUCKET_MODEL_ARTIFACTS: str = config("BUCKET_MODEL_ARTIFACTS")
MODEL_FILENAME: str = config("MODEL_FILENAME")
