# V20CredOfferRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Connection identifier | 
**filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Credential specification criteria by format | 
**auto_issue** | **bool** | Whether to respond automatically to credential requests, creating and issuing requested credentials | [optional] 
**auto_remove** | **bool** | Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting) | [optional] 
**comment** | **str, none_type** | Human-readable comment | [optional] 
**credential_preview** | [**V20CredPreview**](V20CredPreview.md) |  | [optional] 
**trace** | **bool** | Record trace information, based on agent configuration | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


