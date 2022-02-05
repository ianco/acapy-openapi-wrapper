# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.attach_decorator import AttachDecorator


class InvitationMessage(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    InvitationMessage - a model defined in OpenAPI

        id: The id of this InvitationMessage [Optional].
        type: The type of this InvitationMessage [Optional].
        handshake_protocols: The handshake_protocols of this InvitationMessage [Optional].
        label: The label of this InvitationMessage [Optional].
        requestsattach: The requestsattach of this InvitationMessage [Optional].
        services: The services of this InvitationMessage [Optional].
    """

    id: Optional[str] = None
    type: Optional[str] = None
    handshake_protocols: Optional[List[str]] = None
    label: Optional[str] = None
    requestsattach: Optional[List[AttachDecorator]] = None
    services: Optional[List[dict]] = None

InvitationMessage.update_forward_refs()