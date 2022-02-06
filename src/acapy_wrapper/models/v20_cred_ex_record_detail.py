# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.v20_cred_ex_record import V20CredExRecord
from acapy_wrapper.models.v20_cred_ex_record_indy import V20CredExRecordIndy
from acapy_wrapper.models.v20_cred_ex_record_ld_proof import V20CredExRecordLDProof


class V20CredExRecordDetail(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredExRecordDetail - a model defined in OpenAPI

        cred_ex_record: The cred_ex_record of this V20CredExRecordDetail [Optional].
        indy: The indy of this V20CredExRecordDetail [Optional].
        ld_proof: The ld_proof of this V20CredExRecordDetail [Optional].
    """

    cred_ex_record: Optional[V20CredExRecord] = None
    indy: Optional[V20CredExRecordIndy] = None
    ld_proof: Optional[V20CredExRecordLDProof] = None


V20CredExRecordDetail.update_forward_refs()
