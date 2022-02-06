# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class V10CredentialIssueRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialIssueRequest - a model defined in OpenAPI

        comment: The comment of this V10CredentialIssueRequest [Optional].
    """

    comment: Optional[str] = None


V10CredentialIssueRequest.update_forward_refs()
