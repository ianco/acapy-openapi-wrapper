# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class AdminMediationDeny(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AdminMediationDeny - a model defined in OpenAPI

        mediator_terms: The mediator_terms of this AdminMediationDeny [Optional].
        recipient_terms: The recipient_terms of this AdminMediationDeny [Optional].
    """

    mediator_terms: Optional[List[str]] = None
    recipient_terms: Optional[List[str]] = None

AdminMediationDeny.update_forward_refs()