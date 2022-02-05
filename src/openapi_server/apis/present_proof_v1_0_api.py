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
from openapi_server.models.admin_api_message_tracing import AdminAPIMessageTracing
from openapi_server.models.indy_cred_precis import IndyCredPrecis
from openapi_server.models.indy_pres_spec import IndyPresSpec
from openapi_server.models.v10_presentation_create_request_request import V10PresentationCreateRequestRequest
from openapi_server.models.v10_presentation_exchange import V10PresentationExchange
from openapi_server.models.v10_presentation_exchange_list import V10PresentationExchangeList
from openapi_server.models.v10_presentation_problem_report_request import V10PresentationProblemReportRequest
from openapi_server.models.v10_presentation_proposal_request import V10PresentationProposalRequest
from openapi_server.models.v10_presentation_send_request_request import V10PresentationSendRequestRequest
from openapi_server.security_api import get_token_AuthorizationHeader

router = APIRouter()


@router.post(
    "/present-proof/create-request",
    responses={
        200: {"model": V10PresentationExchange, "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Creates a presentation request not bound to any proposal or connection",
)
async def present_proof_create_request_post(
    body: V10PresentationCreateRequestRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10PresentationExchange:
    ...


@router.get(
    "/present-proof/records",
    responses={
        200: {"model": V10PresentationExchangeList, "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Fetch all present-proof exchange records",
)
async def present_proof_records_get(
    connection_id: str = Query(None, description="Connection identifier"),
    role: str = Query(None, description="Role assigned in presentation exchange"),
    state: str = Query(None, description="Presentation exchange state"),
    thread_id: str = Query(None, description="Thread identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10PresentationExchangeList:
    ...


@router.get(
    "/present-proof/records/{pres_ex_id}/credentials",
    responses={
        200: {"model": List[IndyCredPrecis], "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Fetch credentials for a presentation request from wallet",
)
async def present_proof_records_pres_ex_id_credentials_get(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    count: str = Query(None, description="Maximum number to retrieve", regex=r"^[1-9][0-9]*$"),
    extra_query: str = Query(None, description="(JSON) dict mapping referents to extra WQL queries", regex=r"^{\s*&quot;.*?&quot;\s*:\s*{.*?}\s*(,\s*&quot;.*?&quot;\s*:\s*{.*?}\s*)*\s*}$"),
    referent: str = Query(None, description="Proof request referents of interest, comma-separated"),
    start: str = Query(None, description="Start index", regex=r"^[0-9]*$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> List[IndyCredPrecis]:
    ...


@router.delete(
    "/present-proof/records/{pres_ex_id}",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Remove an existing presentation exchange record",
)
async def present_proof_records_pres_ex_id_delete(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...


@router.get(
    "/present-proof/records/{pres_ex_id}",
    responses={
        200: {"model": V10PresentationExchange, "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Fetch a single presentation exchange record",
)
async def present_proof_records_pres_ex_id_get(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10PresentationExchange:
    ...


@router.post(
    "/present-proof/records/{pres_ex_id}/problem-report",
    responses={
        200: {"model": dict, "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Send a problem report for presentation exchange",
)
async def present_proof_records_pres_ex_id_problem_report_post(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V10PresentationProblemReportRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> dict:
    ...


@router.post(
    "/present-proof/records/{pres_ex_id}/send-presentation",
    responses={
        200: {"model": V10PresentationExchange, "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Sends a proof presentation",
)
async def present_proof_records_pres_ex_id_send_presentation_post(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: IndyPresSpec = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10PresentationExchange:
    ...


@router.post(
    "/present-proof/records/{pres_ex_id}/send-request",
    responses={
        200: {"model": V10PresentationExchange, "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Sends a presentation request in reference to a proposal",
)
async def present_proof_records_pres_ex_id_send_request_post(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: AdminAPIMessageTracing = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10PresentationExchange:
    ...


@router.post(
    "/present-proof/records/{pres_ex_id}/verify-presentation",
    responses={
        200: {"model": V10PresentationExchange, "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Verify a received presentation",
)
async def present_proof_records_pres_ex_id_verify_presentation_post(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10PresentationExchange:
    ...


@router.post(
    "/present-proof/send-proposal",
    responses={
        200: {"model": V10PresentationExchange, "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Sends a presentation proposal",
)
async def present_proof_send_proposal_post(
    body: V10PresentationProposalRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10PresentationExchange:
    ...


@router.post(
    "/present-proof/send-request",
    responses={
        200: {"model": V10PresentationExchange, "description": ""},
    },
    tags=["present-proof v1.0"],
    summary="Sends a free presentation request not bound to any proposal",
)
async def present_proof_send_request_post(
    body: V10PresentationSendRequestRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10PresentationExchange:
    ...
