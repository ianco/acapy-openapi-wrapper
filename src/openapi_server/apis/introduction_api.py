# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.security_api import get_token_AuthorizationHeader

router = APIRouter()


@router.post(
    "/connections/{conn_id}/start-introduction",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["introduction"],
    summary="Start an introduction between two connections",
)
async def connections_conn_id_start_introduction_post(
    conn_id: str = Path(None, description="Connection identifier"),
    target_connection_id: str = Query(None, description="Target connection identifier"),
    message: str = Query(None, description="Message"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...
