# IssuerRevRegRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | Time of record creation | [optional] 
**cred_def_id** | **str** | Credential definition identifier | [optional] 
**error_msg** | **str** | Error message | [optional] 
**issuer_did** | **str** | Issuer DID | [optional] 
**max_cred_num** | **int** | Maximum number of credentials for revocation registry | [optional] 
**pending_pub** | **[str]** | Credential revocation identifier for credential revoked and pending publication to ledger | [optional] 
**record_id** | **str** | Issuer revocation registry record identifier | [optional] 
**revoc_def_type** | **str** | Revocation registry type (specify CL_ACCUM) | [optional]  if omitted the server will use the default value of "CL_ACCUM"
**revoc_reg_def** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Revocation registry definition | [optional] 
**revoc_reg_entry** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Revocation registry entry | [optional] 
**revoc_reg_id** | **str** | Revocation registry identifier | [optional] 
**state** | **str** | Issue revocation registry record state | [optional] 
**tag** | **str** | Tag within issuer revocation registry identifier | [optional] 
**tails_hash** | **str** | Tails hash | [optional] 
**tails_local_path** | **str** | Local path to tails file | [optional] 
**tails_public_uri** | **str** | Public URI for tails file | [optional] 
**updated_at** | **str** | Time of last record update | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


