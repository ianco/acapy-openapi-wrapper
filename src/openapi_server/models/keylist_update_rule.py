# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class KeylistUpdateRule(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    KeylistUpdateRule - a model defined in OpenAPI

        action: The action of this KeylistUpdateRule.
        recipient_key: The recipient_key of this KeylistUpdateRule.
    """

    action: str
    recipient_key: str

    @validator("recipient_key")
    def recipient_key_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$", value)
        return value

KeylistUpdateRule.update_forward_refs()
