# IndyProofReqPredSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Attribute name | 
**p_type** | **str** | Predicate type (&#39;&lt;&#39;, &#39;&lt;&#x3D;&#39;, &#39;&gt;&#x3D;&#39;, or &#39;&gt;&#39;) | 
**p_value** | **int** | Threshold value | 
**non_revoked** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**restrictions** | **[{str: (str,)}]** | If present, credential must satisfy one of given restrictions: specify schema_id, schema_issuer_did, schema_name, schema_version, issuer_did, cred_def_id, and/or attr::&lt;attribute-name&gt;::value where &lt;attribute-name&gt; represents a credential attribute name | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


