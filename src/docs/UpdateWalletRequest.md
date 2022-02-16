# UpdateWalletRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | Image url for this wallet. This image url is publicized            (self-attested) to other agents as part of forming a connection. | [optional] 
**label** | **str** | Label for this wallet. This label is publicized            (self-attested) to other agents as part of forming a connection. | [optional] 
**wallet_dispatch_type** | **str** | Webhook target dispatch type for this wallet.             default - Dispatch only to webhooks associated with this wallet.             base - Dispatch only to webhooks associated with the base wallet.             both - Dispatch to both webhook targets. | [optional] 
**wallet_webhook_urls** | **[str]** | List of Webhook URLs associated with this subwallet | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


