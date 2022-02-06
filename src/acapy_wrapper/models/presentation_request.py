# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.attach_decorator import AttachDecorator


class PresentationRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PresentationRequest - a model defined in OpenAPI

        id: The id of this PresentationRequest [Optional].
        type: The type of this PresentationRequest [Optional].
        comment: The comment of this PresentationRequest [Optional].
        request_presentationsattach: The request_presentationsattach of this PresentationRequest.
    """

    id: Optional[str] = None
    type: Optional[str] = None
    comment: Optional[str] = None
    request_presentationsattach: List[AttachDecorator]

PresentationRequest.update_forward_refs()