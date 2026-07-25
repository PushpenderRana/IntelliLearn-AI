"""
JWT issuing/verification for IntelliLearn AI.

Access tokens are stateless — no server-side store, no revoke list.
Logout is handled client-side (frontend drops the token). Good enough
for this project's scope; see README note if you ever need forced
revocation.
"""
import os
from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "change-me-in-prod-use-a-long-random-value")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "1440"))  # 24h default


def create_access_token(data: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    """data should be the bits of the Google userinfo you want to carry,
    e.g. {"sub": user["sub"], "email": user["email"], "name": user["name"], "picture": user.get("picture")}
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict:
    """Raises JWTError on invalid signature or expired token — let caller
    turn that into a 401."""
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


__all__ = ["create_access_token", "decode_access_token", "JWTError"]
