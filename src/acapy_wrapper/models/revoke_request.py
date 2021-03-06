# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class RevokeRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RevokeRequest - a model defined in OpenAPI

        cred_ex_id: The cred_ex_id of this RevokeRequest [Optional].
        cred_rev_id: The cred_rev_id of this RevokeRequest [Optional].
        publish: The publish of this RevokeRequest [Optional].
        rev_reg_id: The rev_reg_id of this RevokeRequest [Optional].
    """

    cred_ex_id: Optional[str] = None
    cred_rev_id: Optional[str] = None
    publish: Optional[bool] = None
    rev_reg_id: Optional[str] = None

    @validator("cred_ex_id")
    def cred_ex_id_pattern(cls, value):
        assert value is not None and re.match(
            r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            value,
        )
        return value

    @validator("cred_rev_id")
    def cred_rev_id_pattern(cls, value):
        assert value is not None and re.match(r"^[1-9][0-9]*$", value)
        return value

    @validator("rev_reg_id")
    def rev_reg_id_pattern(cls, value):
        assert value is not None and re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)",
            value,
        )
        return value


RevokeRequest.update_forward_refs()
