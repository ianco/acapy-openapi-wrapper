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
from acapy_wrapper.models.ping_request import PingRequest
from acapy_wrapper.models.ping_request_response import PingRequestResponse
from acapy_wrapper.security_api import get_token_AuthorizationHeader

router = APIRouter()


@router.post(
    "/connections/{conn_id}/send-ping",
    responses={
        200: {"model": PingRequestResponse, "description": ""},
    },
    tags=["trustping"],
    summary="Send a trust ping to a connection",
)
async def connections_conn_id_send_ping_post(
    conn_id: str = Path(None, description="Connection identifier"),
    body: PingRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> PingRequestResponse:
    ...