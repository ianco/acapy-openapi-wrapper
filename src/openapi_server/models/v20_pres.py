# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.attach_decorator import AttachDecorator
from openapi_server.models.v20_pres_format import V20PresFormat


class V20Pres(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20Pres - a model defined in OpenAPI

        id: The id of this V20Pres [Optional].
        type: The type of this V20Pres [Optional].
        comment: The comment of this V20Pres [Optional].
        formats: The formats of this V20Pres.
        presentationsattach: The presentationsattach of this V20Pres.
    """

    id: Optional[str] = None
    type: Optional[str] = None
    comment: Optional[str] = None
    formats: List[V20PresFormat]
    presentationsattach: List[AttachDecorator]

V20Pres.update_forward_refs()
