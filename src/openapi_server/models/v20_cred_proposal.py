# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.attach_decorator import AttachDecorator
from openapi_server.models.v20_cred_format import V20CredFormat
from openapi_server.models.v20_cred_preview import V20CredPreview


class V20CredProposal(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredProposal - a model defined in OpenAPI

        id: The id of this V20CredProposal [Optional].
        type: The type of this V20CredProposal [Optional].
        comment: The comment of this V20CredProposal [Optional].
        credential_preview: The credential_preview of this V20CredProposal [Optional].
        filtersattach: The filtersattach of this V20CredProposal.
        formats: The formats of this V20CredProposal.
    """

    id: Optional[str] = None
    type: Optional[str] = None
    comment: Optional[str] = None
    credential_preview: Optional[V20CredPreview] = None
    filtersattach: List[AttachDecorator]
    formats: List[V20CredFormat]

V20CredProposal.update_forward_refs()
