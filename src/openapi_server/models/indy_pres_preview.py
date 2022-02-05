# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.indy_pres_attr_spec import IndyPresAttrSpec
from openapi_server.models.indy_pres_pred_spec import IndyPresPredSpec


class IndyPresPreview(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyPresPreview - a model defined in OpenAPI

        type: The type of this IndyPresPreview [Optional].
        attributes: The attributes of this IndyPresPreview.
        predicates: The predicates of this IndyPresPreview.
    """

    type: Optional[str] = None
    attributes: List[IndyPresAttrSpec]
    predicates: List[IndyPresPredSpec]

IndyPresPreview.update_forward_refs()
