# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.credential_definition_send_result import CredentialDefinitionSendResult
from acapy_wrapper.models.transaction_record import TransactionRecord


class TxnOrCredentialDefinitionSendResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TxnOrCredentialDefinitionSendResult - a model defined in OpenAPI

        sent: The sent of this TxnOrCredentialDefinitionSendResult [Optional].
        txn: The txn of this TxnOrCredentialDefinitionSendResult [Optional].
    """

    sent: Optional[CredentialDefinitionSendResult] = None
    txn: Optional[TransactionRecord] = None

TxnOrCredentialDefinitionSendResult.update_forward_refs()