# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class TAAAccept(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TAAAccept - a model defined in OpenAPI

        mechanism: The mechanism of this TAAAccept [Optional].
        text: The text of this TAAAccept [Optional].
        version: The version of this TAAAccept [Optional].
    """

    mechanism: Optional[str] = None
    text: Optional[str] = None
    version: Optional[str] = None

TAAAccept.update_forward_refs()
