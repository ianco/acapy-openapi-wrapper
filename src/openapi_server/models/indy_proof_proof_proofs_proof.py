# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.indy_non_revoc_proof import IndyNonRevocProof
from openapi_server.models.indy_primary_proof import IndyPrimaryProof


class IndyProofProofProofsProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofProofProofsProof - a model defined in OpenAPI

        non_revoc_proof: The non_revoc_proof of this IndyProofProofProofsProof [Optional].
        primary_proof: The primary_proof of this IndyProofProofProofsProof [Optional].
    """

    non_revoc_proof: Optional[IndyNonRevocProof] = None
    primary_proof: Optional[IndyPrimaryProof] = None

IndyProofProofProofsProof.update_forward_refs()