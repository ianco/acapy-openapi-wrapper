# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class SchemaInputDescriptor(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SchemaInputDescriptor - a model defined in OpenAPI

        required: The required of this SchemaInputDescriptor [Optional].
        uri: The uri of this SchemaInputDescriptor [Optional].
    """

    required: Optional[bool] = None
    uri: Optional[str] = None

SchemaInputDescriptor.update_forward_refs()
