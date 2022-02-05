# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class CreateWalletResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateWalletResponse - a model defined in OpenAPI

        created_at: The created_at of this CreateWalletResponse [Optional].
        key_management_mode: The key_management_mode of this CreateWalletResponse.
        settings: The settings of this CreateWalletResponse [Optional].
        state: The state of this CreateWalletResponse [Optional].
        token: The token of this CreateWalletResponse [Optional].
        updated_at: The updated_at of this CreateWalletResponse [Optional].
        wallet_id: The wallet_id of this CreateWalletResponse.
    """

    created_at: Optional[str] = None
    key_management_mode: str
    settings: Optional[Dict[str, Any]] = None
    state: Optional[str] = None
    token: Optional[str] = None
    updated_at: Optional[str] = None
    wallet_id: str

    @validator("created_at")
    def created_at_pattern(cls, value):
        assert value is not None and re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value)
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        assert value is not None and re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value)
        return value

CreateWalletResponse.update_forward_refs()
