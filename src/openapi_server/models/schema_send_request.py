# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class SchemaSendRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SchemaSendRequest - a model defined in OpenAPI

        attributes: The attributes of this SchemaSendRequest.
        schema_name: The schema_name of this SchemaSendRequest.
        schema_version: The schema_version of this SchemaSendRequest.
    """

    attributes: List[str]
    schema_name: str
    schema_version: str

    @validator("schema_version")
    def schema_version_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9.]+$", value)
        return value

SchemaSendRequest.update_forward_refs()