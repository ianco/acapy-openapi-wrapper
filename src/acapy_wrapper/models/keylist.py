# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.route_record import RouteRecord


class Keylist(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Keylist - a model defined in OpenAPI

        results: The results of this Keylist [Optional].
    """

    results: Optional[List[RouteRecord]] = None


Keylist.update_forward_refs()
