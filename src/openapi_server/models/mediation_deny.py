# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class MediationDeny(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MediationDeny - a model defined in OpenAPI

        id: The id of this MediationDeny [Optional].
        type: The type of this MediationDeny [Optional].
        mediator_terms: The mediator_terms of this MediationDeny [Optional].
        recipient_terms: The recipient_terms of this MediationDeny [Optional].
    """

    id: Optional[str] = None
    type: Optional[str] = None
    mediator_terms: Optional[List[str]] = None
    recipient_terms: Optional[List[str]] = None

MediationDeny.update_forward_refs()
