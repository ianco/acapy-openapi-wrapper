# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.keylist_update_rule import KeylistUpdateRule


class KeylistUpdateRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    KeylistUpdateRequest - a model defined in OpenAPI

        updates: The updates of this KeylistUpdateRequest [Optional].
    """

    updates: Optional[List[KeylistUpdateRule]] = None

KeylistUpdateRequest.update_forward_refs()
