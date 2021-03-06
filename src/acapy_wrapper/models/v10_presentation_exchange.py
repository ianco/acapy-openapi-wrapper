# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.indy_proof import IndyProof
from acapy_wrapper.models.indy_proof_request import IndyProofRequest
from acapy_wrapper.models.presentation_proposal import PresentationProposal
from acapy_wrapper.models.presentation_request import PresentationRequest


class V10PresentationExchange(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10PresentationExchange - a model defined in OpenAPI

        auto_present: The auto_present of this V10PresentationExchange [Optional].
        connection_id: The connection_id of this V10PresentationExchange [Optional].
        created_at: The created_at of this V10PresentationExchange [Optional].
        error_msg: The error_msg of this V10PresentationExchange [Optional].
        initiator: The initiator of this V10PresentationExchange [Optional].
        presentation: The presentation of this V10PresentationExchange [Optional].
        presentation_exchange_id: The presentation_exchange_id of this V10PresentationExchange [Optional].
        presentation_proposal_dict: The presentation_proposal_dict of this V10PresentationExchange [Optional].
        presentation_request: The presentation_request of this V10PresentationExchange [Optional].
        presentation_request_dict: The presentation_request_dict of this V10PresentationExchange [Optional].
        role: The role of this V10PresentationExchange [Optional].
        state: The state of this V10PresentationExchange [Optional].
        thread_id: The thread_id of this V10PresentationExchange [Optional].
        trace: The trace of this V10PresentationExchange [Optional].
        updated_at: The updated_at of this V10PresentationExchange [Optional].
        verified: The verified of this V10PresentationExchange [Optional].
    """

    auto_present: Optional[bool] = None
    connection_id: Optional[str] = None
    created_at: Optional[str] = None
    error_msg: Optional[str] = None
    initiator: Optional[str] = None
    presentation: Optional[IndyProof] = None
    presentation_exchange_id: Optional[str] = None
    presentation_proposal_dict: Optional[PresentationProposal] = None
    presentation_request: Optional[IndyProofRequest] = None
    presentation_request_dict: Optional[PresentationRequest] = None
    role: Optional[str] = None
    state: Optional[str] = None
    thread_id: Optional[str] = None
    trace: Optional[bool] = None
    updated_at: Optional[str] = None
    verified: Optional[str] = None

    @validator("created_at")
    def created_at_pattern(cls, value):
        assert value is not None and re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        )
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        assert value is not None and re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        )
        return value


V10PresentationExchange.update_forward_refs()
