# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class V10CredentialProblemReportRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialProblemReportRequest - a model defined in OpenAPI

        description: The description of this V10CredentialProblemReportRequest.
    """

    description: str

V10CredentialProblemReportRequest.update_forward_refs()
