# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.attach_decorator import AttachDecorator
from openapi_server.models.v20_cred_format import V20CredFormat


class V20CredIssue(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredIssue - a model defined in OpenAPI

        id: The id of this V20CredIssue [Optional].
        type: The type of this V20CredIssue [Optional].
        comment: The comment of this V20CredIssue [Optional].
        credentialsattach: The credentialsattach of this V20CredIssue.
        formats: The formats of this V20CredIssue.
        replacement_id: The replacement_id of this V20CredIssue [Optional].
    """

    id: Optional[str] = None
    type: Optional[str] = None
    comment: Optional[str] = None
    credentialsattach: List[AttachDecorator]
    formats: List[V20CredFormat]
    replacement_id: Optional[str] = None

V20CredIssue.update_forward_refs()
