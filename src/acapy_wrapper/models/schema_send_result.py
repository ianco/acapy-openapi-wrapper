# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.schema import Schema


def schema_field(string: str) -> str:
    if string == "schema":
        return "x_schema"
    return string


class SchemaSendResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SchemaSendResult - a model defined in OpenAPI

        schema: The schema of this SchemaSendResult [Optional].
        schema_id: The schema_id of this SchemaSendResult.
    """

    x_schema: Optional[Schema] = None
    schema_id: str

    class Config:
        alias_generator = schema_field

    @validator("schema_id")
    def schema_id_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$", value)
        return value

SchemaSendResult.update_forward_refs()