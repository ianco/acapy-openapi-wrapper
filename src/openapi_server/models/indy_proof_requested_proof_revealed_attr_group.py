# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.raw_encoded import RawEncoded


class IndyProofRequestedProofRevealedAttrGroup(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofRequestedProofRevealedAttrGroup - a model defined in OpenAPI

        sub_proof_index: The sub_proof_index of this IndyProofRequestedProofRevealedAttrGroup [Optional].
        values: The values of this IndyProofRequestedProofRevealedAttrGroup [Optional].
    """

    sub_proof_index: Optional[int] = None
    values: Optional[Dict[str, RawEncoded]] = None

IndyProofRequestedProofRevealedAttrGroup.update_forward_refs()
