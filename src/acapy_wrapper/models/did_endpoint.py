# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class DIDEndpoint(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DIDEndpoint - a model defined in OpenAPI

        did: The did of this DIDEndpoint.
        endpoint: The endpoint of this DIDEndpoint [Optional].
    """

    did: str
    endpoint: Optional[str] = None

    @validator("did")
    def did_pattern(cls, value):
        assert value is not None and re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        )
        return value

    @validator("endpoint")
    def endpoint_pattern(cls, value):
        assert value is not None and re.match(
            r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&amp;#]+)?$",
            value,
        )
        return value


DIDEndpoint.update_forward_refs()
