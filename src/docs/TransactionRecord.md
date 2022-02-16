# TransactionRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Transaction type | [optional] 
**connection_id** | **str** | The connection identifier for thie particular transaction record | [optional] 
**created_at** | **str** | Time of record creation | [optional] 
**endorser_write_txn** | **bool** | If True, Endorser will write the transaction after endorsing it | [optional] 
**formats** | **[{str: (str,)}]** |  | [optional] 
**messages_attach** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**meta_data** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**signature_request** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**signature_response** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**state** | **str** | Current record state | [optional] 
**thread_id** | **str** | Thread Identifier | [optional] 
**timing** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**trace** | **bool** | Record trace information, based on agent configuration | [optional] 
**transaction_id** | **str** | Transaction identifier | [optional] 
**updated_at** | **str** | Time of last record update | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


