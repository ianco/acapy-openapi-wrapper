# openapi_client.OutOfBandApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**out_of_band_create_invitation_post**](OutOfBandApi.md#out_of_band_create_invitation_post) | **POST** /out-of-band/create-invitation | Create a new connection invitation
[**out_of_band_receive_invitation_post**](OutOfBandApi.md#out_of_band_receive_invitation_post) | **POST** /out-of-band/receive-invitation | Receive a new connection invitation


# **out_of_band_create_invitation_post**
> InvitationRecord out_of_band_create_invitation_post()

Create a new connection invitation

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import out_of_band_api
from openapi_client.model.invitation_create_request import InvitationCreateRequest
from openapi_client.model.invitation_record import InvitationRecord
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthorizationHeader
configuration.api_key['AuthorizationHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = out_of_band_api.OutOfBandApi(api_client)
    auto_accept = True # bool | Auto-accept connection (defaults to configuration) (optional)
    multi_use = True # bool | Create invitation for multiple use (default false) (optional)
    body = InvitationCreateRequest(
        alias="Barry",
        attachments=[
            AttachmentDef(
                id="attachment-0",
                type="present-proof",
            ),
        ],
        handshake_protocols=[
            "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0",
        ],
        mediation_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        metadata={},
        my_label="Invitation to Barry",
        use_public_did=False,
    ) # InvitationCreateRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new connection invitation
        api_response = api_instance.out_of_band_create_invitation_post(auto_accept=auto_accept, multi_use=multi_use, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OutOfBandApi->out_of_band_create_invitation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_accept** | **bool**| Auto-accept connection (defaults to configuration) | [optional]
 **multi_use** | **bool**| Create invitation for multiple use (default false) | [optional]
 **body** | [**InvitationCreateRequest**](InvitationCreateRequest.md)|  | [optional]

### Return type

[**InvitationRecord**](InvitationRecord.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **out_of_band_receive_invitation_post**
> ConnRecord out_of_band_receive_invitation_post()

Receive a new connection invitation

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import out_of_band_api
from openapi_client.model.conn_record import ConnRecord
from openapi_client.model.invitation_message import InvitationMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthorizationHeader
configuration.api_key['AuthorizationHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = out_of_band_api.OutOfBandApi(api_client)
    alias = "alias_example" # str | Alias for connection (optional)
    auto_accept = True # bool | Auto-accept connection (defaults to configuration) (optional)
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    use_existing_connection = True # bool | Use an existing connection, if possible (optional)
    body = InvitationMessage(
        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        handshake_protocols=[
            "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0",
        ],
        label="Bob",
        requestsattach=[
            AttachDecorator(
                id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
                byte_count=1234,
                data=AttachDecoratorData(
                    base64="ey4uLn0=",
                    json={},
                    jws={},
                    links=[
                        "https://link.to/data",
                    ],
                    sha256="617a48c7c8afe0521efdc03e5bb0ad9e655893e6b4b51f0e794d70fba132aacb",
                ),
                description="view from doorway, facing east, with lights off",
                filename="IMG1092348.png",
                lastmod_time="2021-12-31T23:59:59Z",
                mime_type="image/png",
            ),
        ],
        services=[{did=WgWxqztrNooG92RXvxSTWv, id=string, recipientKeys=[did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH], routingKeys=[did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH], serviceEndpoint=http://192.168.56.101:8020, type=string}, did:sov:WgWxqztrNooG92RXvxSTWv],
    ) # InvitationMessage |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Receive a new connection invitation
        api_response = api_instance.out_of_band_receive_invitation_post(alias=alias, auto_accept=auto_accept, mediation_id=mediation_id, use_existing_connection=use_existing_connection, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OutOfBandApi->out_of_band_receive_invitation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias for connection | [optional]
 **auto_accept** | **bool**| Auto-accept connection (defaults to configuration) | [optional]
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
 **use_existing_connection** | **bool**| Use an existing connection, if possible | [optional]
 **body** | [**InvitationMessage**](InvitationMessage.md)|  | [optional]

### Return type

[**ConnRecord**](ConnRecord.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

