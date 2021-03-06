# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.indy_rev_reg_def import IndyRevRegDef
from acapy_wrapper.models.indy_rev_reg_entry import IndyRevRegEntry


class IssuerRevRegRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IssuerRevRegRecord - a model defined in OpenAPI

        created_at: The created_at of this IssuerRevRegRecord [Optional].
        cred_def_id: The cred_def_id of this IssuerRevRegRecord [Optional].
        error_msg: The error_msg of this IssuerRevRegRecord [Optional].
        issuer_did: The issuer_did of this IssuerRevRegRecord [Optional].
        max_cred_num: The max_cred_num of this IssuerRevRegRecord [Optional].
        pending_pub: The pending_pub of this IssuerRevRegRecord [Optional].
        record_id: The record_id of this IssuerRevRegRecord [Optional].
        revoc_def_type: The revoc_def_type of this IssuerRevRegRecord [Optional].
        revoc_reg_def: The revoc_reg_def of this IssuerRevRegRecord [Optional].
        revoc_reg_entry: The revoc_reg_entry of this IssuerRevRegRecord [Optional].
        revoc_reg_id: The revoc_reg_id of this IssuerRevRegRecord [Optional].
        state: The state of this IssuerRevRegRecord [Optional].
        tag: The tag of this IssuerRevRegRecord [Optional].
        tails_hash: The tails_hash of this IssuerRevRegRecord [Optional].
        tails_local_path: The tails_local_path of this IssuerRevRegRecord [Optional].
        tails_public_uri: The tails_public_uri of this IssuerRevRegRecord [Optional].
        updated_at: The updated_at of this IssuerRevRegRecord [Optional].
    """

    created_at: Optional[str] = None
    cred_def_id: Optional[str] = None
    error_msg: Optional[str] = None
    issuer_did: Optional[str] = None
    max_cred_num: Optional[int] = None
    pending_pub: Optional[List[str]] = None
    record_id: Optional[str] = None
    revoc_def_type: Optional[str] = None
    revoc_reg_def: Optional[IndyRevRegDef] = None
    revoc_reg_entry: Optional[IndyRevRegEntry] = None
    revoc_reg_id: Optional[str] = None
    state: Optional[str] = None
    tag: Optional[str] = None
    tails_hash: Optional[str] = None
    tails_local_path: Optional[str] = None
    tails_public_uri: Optional[str] = None
    updated_at: Optional[str] = None

    @validator("created_at")
    def created_at_pattern(cls, value):
        assert value is not None and re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        )
        return value

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):
        assert value is not None and re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$",
            value,
        )
        return value

    @validator("issuer_did")
    def issuer_did_pattern(cls, value):
        assert value is not None and re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        )
        return value

    @validator("revoc_reg_id")
    def revoc_reg_id_pattern(cls, value):
        assert value is not None and re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)",
            value,
        )
        return value

    @validator("tails_hash")
    def tails_hash_pattern(cls, value):
        assert value is not None and re.match(
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$",
            value,
        )
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        assert value is not None and re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        )
        return value


IssuerRevRegRecord.update_forward_refs()
