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
from acapy_wrapper.models.action_menu_fetch_result import ActionMenuFetchResult
from acapy_wrapper.models.perform_request import PerformRequest
from acapy_wrapper.models.send_menu import SendMenu
from acapy_wrapper.security_api import get_token_AuthorizationHeader

router = APIRouter()


@router.post(
    "/action-menu/{conn_id}/close",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["action-menu"],
    summary="Close the active menu associated with a connection",
)
async def action_menu_conn_id_close_post(
    conn_id: str = Path(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...


@router.post(
    "/action-menu/{conn_id}/fetch",
    responses={
        200: {"model": ActionMenuFetchResult, "description": ""},
    },
    tags=["action-menu"],
    summary="Fetch the active menu",
)
async def action_menu_conn_id_fetch_post(
    conn_id: str = Path(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ActionMenuFetchResult:
    ...


@router.post(
    "/action-menu/{conn_id}/perform",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["action-menu"],
    summary="Perform an action associated with the active menu",
)
async def action_menu_conn_id_perform_post(
    conn_id: str = Path(None, description="Connection identifier"),
    body: PerformRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...


@router.post(
    "/action-menu/{conn_id}/request",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["action-menu"],
    summary="Request the active menu",
)
async def action_menu_conn_id_request_post(
    conn_id: str = Path(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...


@router.post(
    "/action-menu/{conn_id}/send-menu",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["action-menu"],
    summary="Send an action menu to a connection",
)
async def action_menu_conn_id_send_menu_post(
    conn_id: str = Path(None, description="Connection identifier"),
    body: SendMenu = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...
