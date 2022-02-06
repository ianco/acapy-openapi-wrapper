# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Filter(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Filter - a model defined in OpenAPI

        const: The const of this Filter [Optional].
        enum: The enum of this Filter [Optional].
        exclusive_maximum: The exclusive_maximum of this Filter [Optional].
        exclusive_minimum: The exclusive_minimum of this Filter [Optional].
        format: The format of this Filter [Optional].
        max_length: The max_length of this Filter [Optional].
        maximum: The maximum of this Filter [Optional].
        min_length: The min_length of this Filter [Optional].
        minimum: The minimum of this Filter [Optional].
        _not: The _not of this Filter [Optional].
        pattern: The pattern of this Filter [Optional].
        type: The type of this Filter [Optional].
    """

    const: Optional[Dict[str, Any]] = None
    enum: Optional[List[dict]] = None
    exclusive_maximum: Optional[Dict[str, Any]] = None
    exclusive_minimum: Optional[Dict[str, Any]] = None
    format: Optional[str] = None
    max_length: Optional[int] = None
    maximum: Optional[Dict[str, Any]] = None
    min_length: Optional[int] = None
    minimum: Optional[Dict[str, Any]] = None
    _not: Optional[bool] = None
    pattern: Optional[str] = None
    type: Optional[str] = None


Filter.update_forward_refs()
