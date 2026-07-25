import os
import secrets
from typing import Optional

from fastapi import APIRouter, Header, HTTPException, Request
from pydantic import BaseModel
from starlette.responses import RedirectResponse

from app.auth.config import oauth
from app.auth.jwt import create_access_token, decode_access_token, JWTError


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

FRONTEND_URL = os.getenv(
    "INTELLILEARN_FRONTEND_URL",
    "https://intellilearn-ai-judvr8fdoxyygscdyxfzng.streamlit.app/"
)

# Temporary in-memory storage
# temp_code -> jwt_token
temp_codes = {}


class ExchangeRequest(BaseModel):
    code: str


@router.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for("auth_callback")
    return await oauth.google.authorize_redirect(
        request,
        redirect_uri
    )


@router.get("/callback", name="auth_callback")
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)

    user = token.get("userinfo")

    jwt_token = create_access_token(
        {
            "sub": user.get("sub"),
            "email": user.get("email"),
            "name": user.get("name"),
            "picture": user.get("picture"),
        }
    )

    # Generate temporary authorization code
    temp_code = secrets.token_urlsafe(32)

    # Store JWT against temporary code
    temp_codes[temp_code] = jwt_token

    # Redirect WITHOUT exposing JWT
    return RedirectResponse(
        url=f"{FRONTEND_URL}/?code={temp_code}"
    )


@router.post("/exchange")
async def exchange(request: ExchangeRequest):
    jwt_token = temp_codes.pop(request.code, None)

    if jwt_token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired authorization code."
        )

    return {
        "access_token": jwt_token,
        "token_type": "Bearer"
    }


@router.get("/logout")
async def logout():
    return {
        "message": "Logged Out"
    }


@router.get("/me")
async def me(
    authorization: Optional[str] = Header(default=None)
):
    if (
        not authorization
        or not authorization.lower().startswith("bearer ")
    ):
        return {
            "authenticated": False
        }

    token = authorization.split(" ", 1)[1].strip()

    try:
        payload = decode_access_token(token)

        return {
            "authenticated": True,
            "user": payload
        }

    except JWTError:
        return {
            "authenticated": False
        }