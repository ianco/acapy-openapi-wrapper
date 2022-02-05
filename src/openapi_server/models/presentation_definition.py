# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.claim_format import ClaimFormat
from openapi_server.models.input_descriptors import InputDescriptors
from openapi_server.models.submission_requirements import SubmissionRequirements


class PresentationDefinition(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PresentationDefinition - a model defined in OpenAPI

        format: The format of this PresentationDefinition [Optional].
        id: The id of this PresentationDefinition [Optional].
        input_descriptors: The input_descriptors of this PresentationDefinition [Optional].
        name: The name of this PresentationDefinition [Optional].
        purpose: The purpose of this PresentationDefinition [Optional].
        submission_requirements: The submission_requirements of this PresentationDefinition [Optional].
    """

    format: Optional[ClaimFormat] = None
    id: Optional[str] = None
    input_descriptors: Optional[List[InputDescriptors]] = None
    name: Optional[str] = None
    purpose: Optional[str] = None
    submission_requirements: Optional[List[SubmissionRequirements]] = None

    @validator("id")
    def id_pattern(cls, value):
        assert value is not None and re.match(r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}", value)
        return value

PresentationDefinition.update_forward_refs()