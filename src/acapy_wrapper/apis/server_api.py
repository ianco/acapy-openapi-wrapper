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

from acapy_wrapper.models.extra_models import TokenModel  # noqa: F401
from acapy_wrapper.models.admin_config import AdminConfig
from acapy_wrapper.models.admin_modules import AdminModules
from acapy_wrapper.models.admin_status import AdminStatus
from acapy_wrapper.models.admin_status_liveliness import AdminStatusLiveliness
from acapy_wrapper.models.admin_status_readiness import AdminStatusReadiness
from acapy_wrapper.models.query_result import QueryResult
from acapy_wrapper.security_api import get_token_AuthorizationHeader

router = APIRouter()


@router.get(
    "/features",
    responses={
        200: {"model": QueryResult, "description": ""},
    },
    tags=["server"],
    summary="Query supported features",
)
async def features_get(
    query: str = Query(None, description="Query"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> QueryResult:
    ...


@router.get(
    "/plugins",
    responses={
        200: {"model": AdminModules, "description": ""},
    },
    tags=["server"],
    summary="Fetch the list of loaded plugins",
)
async def plugins_get(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AdminModules:
    ...


@router.get(
    "/shutdown",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["server"],
    summary="Shut down server",
)
async def shutdown_get(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...


@router.get(
    "/status/config",
    responses={
        200: {"model": AdminConfig, "description": ""},
    },
    tags=["server"],
    summary="Fetch the server configuration",
)
async def status_config_get(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AdminConfig:
    ...


@router.get(
    "/status",
    responses={
        200: {"model": AdminStatus, "description": ""},
    },
    tags=["server"],
    summary="Fetch the server status",
)
async def status_get(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AdminStatus:
    ...


@router.get(
    "/status/live",
    responses={
        200: {"model": AdminStatusLiveliness, "description": ""},
    },
    tags=["server"],
    summary="Liveliness check",
)
async def status_live_get(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AdminStatusLiveliness:
    ...


@router.get(
    "/status/ready",
    responses={
        200: {"model": AdminStatusReadiness, "description": ""},
    },
    tags=["server"],
    summary="Readiness check",
)
async def status_ready_get(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AdminStatusReadiness:
    ...


@router.post(
    "/status/reset",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["server"],
    summary="Reset statistics",
)
async def status_reset_post(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...
