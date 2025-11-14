from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()
cors = CORS()

limits_env = os.getenv("RATELIMIT_DEFAULT_LIMITS", "1000 per day;200 per hour;50 per minute")
default_limits = [l.strip() for l in limits_env.split(";") if l.strip()]
storage_uri = os.getenv("RATELIMIT_STORAGE_URI", "memory://")
enabled_env = os.getenv("RATELIMIT_ENABLED", "true").lower()
enabled = enabled_env in ("1", "true", "yes")

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=default_limits,
    storage_uri=storage_uri,
    enabled=enabled,
)