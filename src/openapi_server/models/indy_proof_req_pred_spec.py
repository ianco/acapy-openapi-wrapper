# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.indy_proof_req_pred_spec_non_revoked import IndyProofReqPredSpecNonRevoked


class IndyProofReqPredSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofReqPredSpec - a model defined in OpenAPI

        name: The name of this IndyProofReqPredSpec.
        non_revoked: The non_revoked of this IndyProofReqPredSpec [Optional].
        p_type: The p_type of this IndyProofReqPredSpec.
        p_value: The p_value of this IndyProofReqPredSpec.
        restrictions: The restrictions of this IndyProofReqPredSpec [Optional].
    """

    name: str
    non_revoked: Optional[IndyProofReqPredSpecNonRevoked] = None
    p_type: str
    p_value: int
    restrictions: Optional[List[Dict[str, str]]] = None

IndyProofReqPredSpec.update_forward_refs()
