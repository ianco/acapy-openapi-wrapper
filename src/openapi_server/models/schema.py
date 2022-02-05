# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Schema(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Schema - a model defined in OpenAPI

        attr_names: The attr_names of this Schema [Optional].
        id: The id of this Schema [Optional].
        name: The name of this Schema [Optional].
        seq_no: The seq_no of this Schema [Optional].
        ver: The ver of this Schema [Optional].
        version: The version of this Schema [Optional].
    """

    attr_names: Optional[List[str]] = None
    id: Optional[str] = None
    name: Optional[str] = None
    seq_no: Optional[int] = None
    ver: Optional[str] = None
    version: Optional[str] = None

    @validator("id")
    def id_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$", value)
        return value

    @validator("seq_no")
    def seq_no_min(cls, value):
        assert value >= 1
        return value

    @validator("ver")
    def ver_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9.]+$", value)
        return value

    @validator("version")
    def version_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9.]+$", value)
        return value

Schema.update_forward_refs()
