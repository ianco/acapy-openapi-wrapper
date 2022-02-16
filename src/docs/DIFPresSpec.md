# DIFPresSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_id** | **str** | Issuer identifier to sign the presentation, if different from current public DID | [optional] 
**presentation_definition** | [**PresentationDefinition**](PresentationDefinition.md) |  | [optional] 
**record_ids** | **bool, date, datetime, dict, float, int, list, str, none_type** | Mapping of input_descriptor id to list of stored W3C credential record_id | [optional] 
**reveal_doc** | **bool, date, datetime, dict, float, int, list, str, none_type** | reveal doc [JSON-LD frame] dict used to derive the credential when selective disclosure is required | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


