# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.indy_cred_info import IndyCredInfo
from openapi_server.models.indy_non_revocation_interval import IndyNonRevocationInterval


class IndyCredPrecis(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyCredPrecis - a model defined in OpenAPI

        cred_info: The cred_info of this IndyCredPrecis [Optional].
        interval: The interval of this IndyCredPrecis [Optional].
        presentation_referents: The presentation_referents of this IndyCredPrecis [Optional].
    """

    cred_info: Optional[IndyCredInfo] = None
    interval: Optional[IndyNonRevocationInterval] = None
    presentation_referents: Optional[List[str]] = None

IndyCredPrecis.update_forward_refs()
