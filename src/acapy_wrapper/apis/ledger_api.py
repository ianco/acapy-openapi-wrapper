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
from acapy_wrapper.models.get_did_endpoint_response import GetDIDEndpointResponse
from acapy_wrapper.models.get_did_verkey_response import GetDIDVerkeyResponse
from acapy_wrapper.models.get_nym_role_response import GetNymRoleResponse
from acapy_wrapper.models.register_ledger_nym_response import RegisterLedgerNymResponse
from acapy_wrapper.models.taa_accept import TAAAccept
from acapy_wrapper.models.taa_result import TAAResult
from acapy_wrapper.security_api import get_token_AuthorizationHeader

router = APIRouter()


@router.get(
    "/ledger/did-endpoint",
    responses={
        200: {"model": GetDIDEndpointResponse, "description": ""},
    },
    tags=["ledger"],
    summary="Get the endpoint for a DID from the ledger.",
)
async def ledger_did_endpoint_get(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    endpoint_type: str = Query(None, description="Endpoint type of interest (default &#39;Endpoint&#39;)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> GetDIDEndpointResponse:
    ...


@router.get(
    "/ledger/did-verkey",
    responses={
        200: {"model": GetDIDVerkeyResponse, "description": ""},
    },
    tags=["ledger"],
    summary="Get the verkey for a DID from the ledger.",
)
async def ledger_did_verkey_get(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> GetDIDVerkeyResponse:
    ...


@router.get(
    "/ledger/get-nym-role",
    responses={
        200: {"model": GetNymRoleResponse, "description": ""},
    },
    tags=["ledger"],
    summary="Get the role from the NYM registration of a public DID.",
)
async def ledger_get_nym_role_get(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> GetNymRoleResponse:
    ...


@router.post(
    "/ledger/register-nym",
    responses={
        200: {"model": RegisterLedgerNymResponse, "description": ""},
    },
    tags=["ledger"],
    summary="Send a NYM registration to the ledger.",
)
async def ledger_register_nym_post(
    did: str = Query(None, description="DID to register", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    verkey: str = Query(None, description="Verification key", regex=r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"),
    alias: str = Query(None, description="Alias"),
    role: str = Query(None, description="Role"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> RegisterLedgerNymResponse:
    ...


@router.patch(
    "/ledger/rotate-public-did-keypair",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["ledger"],
    summary="Rotate key pair for public DID.",
)
async def ledger_rotate_public_did_keypair_patch(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...


@router.post(
    "/ledger/taa/accept",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["ledger"],
    summary="Accept the transaction author agreement",
)
async def ledger_taa_accept_post(
    body: TAAAccept = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...


@router.get(
    "/ledger/taa",
    responses={
        200: {"model": TAAResult, "description": ""},
    },
    tags=["ledger"],
    summary="Fetch the current transaction author agreement, if any",
)
async def ledger_taa_get(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TAAResult:
    ...
