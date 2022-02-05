# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.indy_requested_creds_requested_attr import IndyRequestedCredsRequestedAttr
from openapi_server.models.indy_requested_creds_requested_pred import IndyRequestedCredsRequestedPred


class IndyPresSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyPresSpec - a model defined in OpenAPI

        requested_attributes: The requested_attributes of this IndyPresSpec.
        requested_predicates: The requested_predicates of this IndyPresSpec.
        self_attested_attributes: The self_attested_attributes of this IndyPresSpec.
        trace: The trace of this IndyPresSpec [Optional].
    """

    requested_attributes: Dict[str, IndyRequestedCredsRequestedAttr]
    requested_predicates: Dict[str, IndyRequestedCredsRequestedPred]
    self_attested_attributes: Dict[str, str]
    trace: Optional[bool] = None

IndyPresSpec.update_forward_refs()
