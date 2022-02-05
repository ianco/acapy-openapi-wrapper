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
from openapi_server.models.did_create import DIDCreate
from openapi_server.models.did_endpoint import DIDEndpoint
from openapi_server.models.did_endpoint_with_type import DIDEndpointWithType
from openapi_server.models.did_list import DIDList
from openapi_server.models.did_result import DIDResult
from openapi_server.security_api import get_token_AuthorizationHeader

router = APIRouter()


@router.post(
    "/wallet/did/create",
    responses={
        200: {"model": DIDResult, "description": ""},
    },
    tags=["wallet"],
    summary="Create a local DID",
)
async def wallet_did_create_post(
    body: DIDCreate = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> DIDResult:
    ...


@router.get(
    "/wallet/did",
    responses={
        200: {"model": DIDList, "description": ""},
    },
    tags=["wallet"],
    summary="List wallet DIDs",
)
async def wallet_did_get(
    did: str = Query(None, description="DID of interest", regex=r"^did:key:z[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]+$|^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    key_type: str = Query(None, description="Key type to query for."),
    method: str = Query(None, description="DID method to query for. e.g. sov to only fetch indy/sov DIDs"),
    posture: str = Query(None, description="Whether DID is current public DID, posted to ledger but current public DID, or local to the wallet"),
    verkey: str = Query(None, description="Verification key of interest", regex=r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> DIDList:
    ...


@router.patch(
    "/wallet/did/local/rotate-keypair",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["wallet"],
    summary="Rotate keypair for a DID not posted to the ledger",
)
async def wallet_did_local_rotate_keypair_patch(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...


@router.get(
    "/wallet/did/public",
    responses={
        200: {"model": DIDResult, "description": ""},
    },
    tags=["wallet"],
    summary="Fetch the current public DID",
)
async def wallet_did_public_get(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> DIDResult:
    ...


@router.post(
    "/wallet/did/public",
    responses={
        200: {"model": DIDResult, "description": ""},
    },
    tags=["wallet"],
    summary="Assign the current public DID",
)
async def wallet_did_public_post(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> DIDResult:
    ...


@router.get(
    "/wallet/get-did-endpoint",
    responses={
        200: {"model": DIDEndpoint, "description": ""},
    },
    tags=["wallet"],
    summary="Query DID endpoint in wallet",
)
async def wallet_get_did_endpoint_get(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> DIDEndpoint:
    ...


@router.post(
    "/wallet/set-did-endpoint",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["wallet"],
    summary="Update endpoint in wallet and on ledger if posted to it",
)
async def wallet_set_did_endpoint_post(
    body: DIDEndpointWithType = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...
