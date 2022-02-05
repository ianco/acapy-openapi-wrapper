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
from openapi_server.models.sign_request import SignRequest
from openapi_server.models.sign_response import SignResponse
from openapi_server.models.verify_request import VerifyRequest
from openapi_server.models.verify_response import VerifyResponse
from openapi_server.security_api import get_token_AuthorizationHeader

router = APIRouter()


@router.post(
    "/jsonld/sign",
    responses={
        200: {"model": SignResponse, "description": ""},
    },
    tags=["jsonld"],
    summary="Sign a JSON-LD structure and return it",
)
async def jsonld_sign_post(
    body: SignRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> SignResponse:
    ...


@router.post(
    "/jsonld/verify",
    responses={
        200: {"model": VerifyResponse, "description": ""},
    },
    tags=["jsonld"],
    summary="Verify a JSON-LD structure.",
)
async def jsonld_verify_post(
    body: VerifyRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> VerifyResponse:
    ...
