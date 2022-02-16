# LinkedDataProof


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | The string value of an ISO8601 combined date and time string generated by the Signature Algorithm | 
**proof_purpose** | **str** | Proof purpose | 
**type** | **str** | Identifies the digital signature suite that was used to create the signature | 
**verification_method** | **str** | Information used for proof verification | 
**challenge** | **str** | Associates a challenge with a proof, for use with a proofPurpose such as authentication | [optional] 
**domain** | **str** | A string value specifying the restricted domain of the signature. | [optional] 
**jws** | **str** | Associates a Detached Json Web Signature with a proof | [optional] 
**nonce** | **str** | The nonce | [optional] 
**proof_value** | **str** | The proof value of a proof | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

