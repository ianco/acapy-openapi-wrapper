# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class IndyRevRegEntryValue(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyRevRegEntryValue - a model defined in OpenAPI

        accum: The accum of this IndyRevRegEntryValue [Optional].
        prev_accum: The prev_accum of this IndyRevRegEntryValue [Optional].
        revoked: The revoked of this IndyRevRegEntryValue [Optional].
    """

    accum: Optional[str] = None
    prev_accum: Optional[str] = None
    revoked: Optional[List[int]] = None

IndyRevRegEntryValue.update_forward_refs()
