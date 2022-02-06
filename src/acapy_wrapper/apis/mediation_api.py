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
from acapy_wrapper.models.admin_mediation_deny import AdminMediationDeny
from acapy_wrapper.models.keylist import Keylist
from acapy_wrapper.models.keylist_query import KeylistQuery
from acapy_wrapper.models.keylist_query_filter_request import KeylistQueryFilterRequest
from acapy_wrapper.models.keylist_update import KeylistUpdate
from acapy_wrapper.models.keylist_update_request import KeylistUpdateRequest
from acapy_wrapper.models.mediation_create_request import MediationCreateRequest
from acapy_wrapper.models.mediation_deny import MediationDeny
from acapy_wrapper.models.mediation_grant import MediationGrant
from acapy_wrapper.models.mediation_list import MediationList
from acapy_wrapper.models.mediation_record import MediationRecord
from acapy_wrapper.security_api import get_token_AuthorizationHeader

router = APIRouter()


@router.delete(
    "/mediation/default-mediator",
    responses={
        201: {"model": MediationRecord, "description": "null"},
    },
    tags=["mediation"],
    summary="Clear default mediator",
)
async def mediation_default_mediator_delete(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.get(
    "/mediation/default-mediator",
    responses={
        200: {"model": MediationRecord, "description": "null"},
    },
    tags=["mediation"],
    summary="Get default mediator",
)
async def mediation_default_mediator_get(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.get(
    "/mediation/keylists",
    responses={
        200: {"model": Keylist, "description": "null"},
    },
    tags=["mediation"],
    summary="Retrieve keylists by connection or role",
)
async def mediation_keylists_get(
    conn_id: str = Query(None, description="Connection identifier (optional)"),
    role: str = Query("server", description="Filer on role, &#39;client&#39; for keys         mediated by other agents, &#39;server&#39; for keys         mediated by this agent"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> Keylist:
    ...


@router.post(
    "/mediation/keylists/{mediation_id}/send-keylist-query",
    responses={
        201: {"model": KeylistQuery, "description": "null"},
    },
    tags=["mediation"],
    summary="Send keylist query to mediator",
)
async def mediation_keylists_mediation_id_send_keylist_query_post(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    paginate_limit: int = Query(-1, description="limit number of results"),
    paginate_offset: int = Query(0, description="offset to use in pagination"),
    body: KeylistQueryFilterRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> KeylistQuery:
    ...


@router.post(
    "/mediation/keylists/{mediation_id}/send-keylist-update",
    responses={
        201: {"model": KeylistUpdate, "description": "null"},
    },
    tags=["mediation"],
    summary="Send keylist update to mediator",
)
async def mediation_keylists_mediation_id_send_keylist_update_post(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    body: KeylistUpdateRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> KeylistUpdate:
    ...


@router.put(
    "/mediation/{mediation_id}/default-mediator",
    responses={
        201: {"model": MediationRecord, "description": "null"},
    },
    tags=["mediation"],
    summary="Set default mediator",
)
async def mediation_mediation_id_default_mediator_put(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.post(
    "/mediation/request/{conn_id}",
    responses={
        201: {"model": MediationRecord, "description": "null"},
    },
    tags=["mediation"],
    summary="Request mediation from connection",
)
async def mediation_request_conn_id_post(
    conn_id: str = Path(None, description="Connection identifier"),
    body: MediationCreateRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.get(
    "/mediation/requests",
    responses={
        200: {"model": MediationList, "description": "null"},
    },
    tags=["mediation"],
    summary="Query mediation requests, returns list of all mediation records",
)
async def mediation_requests_get(
    conn_id: str = Query(None, description="Connection identifier (optional)"),
    mediator_terms: List[str] = Query(None, description="List of mediator rules for recipient"),
    recipient_terms: List[str] = Query(None, description="List of recipient rules for mediation"),
    state: str = Query(None, description="Mediation state (optional)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationList:
    ...


@router.delete(
    "/mediation/requests/{mediation_id}",
    responses={
        200: {"model": MediationRecord, "description": "null"},
    },
    tags=["mediation"],
    summary="Delete mediation request by ID",
)
async def mediation_requests_mediation_id_delete(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.post(
    "/mediation/requests/{mediation_id}/deny",
    responses={
        201: {"model": MediationDeny, "description": "null"},
    },
    tags=["mediation"],
    summary="Deny a stored mediation request",
)
async def mediation_requests_mediation_id_deny_post(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    body: AdminMediationDeny = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationDeny:
    ...


@router.get(
    "/mediation/requests/{mediation_id}",
    responses={
        200: {"model": MediationRecord, "description": "null"},
    },
    tags=["mediation"],
    summary="Retrieve mediation request record",
)
async def mediation_requests_mediation_id_get(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.post(
    "/mediation/requests/{mediation_id}/grant",
    responses={
        201: {"model": MediationGrant, "description": "null"},
    },
    tags=["mediation"],
    summary="Grant received mediation",
)
async def mediation_requests_mediation_id_grant_post(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationGrant:
    ...
