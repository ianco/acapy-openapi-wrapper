# V20CredRequestFree


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Connection identifier | 
**filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Credential specification criteria by format | 
**auto_remove** | **bool** | Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting) | [optional] 
**comment** | **str, none_type** | Human-readable comment | [optional] 
**holder_did** | **str, none_type** | Holder DID to substitute for the credentialSubject.id | [optional] 
**trace** | **bool** | Whether to trace event (default false) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


