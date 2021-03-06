# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.taa_info import TAAInfo


class TAAResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TAAResult - a model defined in OpenAPI

        result: The result of this TAAResult [Optional].
    """

    result: Optional[TAAInfo] = None


TAAResult.update_forward_refs()
