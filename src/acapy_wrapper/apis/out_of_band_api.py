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
from acapy_wrapper.models.conn_record import ConnRecord
from acapy_wrapper.models.invitation_create_request import InvitationCreateRequest
from acapy_wrapper.models.invitation_message import InvitationMessage
from acapy_wrapper.models.invitation_record import InvitationRecord
from acapy_wrapper.security_api import get_token_AuthorizationHeader

router = APIRouter()


@router.post(
    "/out-of-band/create-invitation",
    responses={
        200: {"model": InvitationRecord, "description": ""},
    },
    tags=["out-of-band"],
    summary="Create a new connection invitation",
)
async def out_of_band_create_invitation_post(
    auto_accept: bool = Query(None, description="Auto-accept connection (defaults to configuration)"),
    multi_use: bool = Query(None, description="Create invitation for multiple use (default false)"),
    body: InvitationCreateRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> InvitationRecord:
    ...


@router.post(
    "/out-of-band/receive-invitation",
    responses={
        200: {"model": ConnRecord, "description": ""},
    },
    tags=["out-of-band"],
    summary="Receive a new connection invitation",
)
async def out_of_band_receive_invitation_post(
    alias: str = Query(None, description="Alias for connection"),
    auto_accept: bool = Query(None, description="Auto-accept connection (defaults to configuration)"),
    mediation_id: str = Query(None, description="Identifier for active mediation record to be used", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    use_existing_connection: bool = Query(None, description="Use an existing connection, if possible"),
    body: InvitationMessage = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnRecord:
    ...
