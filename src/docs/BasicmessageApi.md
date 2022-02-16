# openapi_client.BasicmessageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connections_conn_id_send_message_post**](BasicmessageApi.md#connections_conn_id_send_message_post) | **POST** /connections/{conn_id}/send-message | Send a basic message to a connection


# **connections_conn_id_send_message_post**
> bool, date, datetime, dict, float, int, list, str, none_type connections_conn_id_send_message_post(conn_id)

Send a basic message to a connection

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import basicmessage_api
from openapi_client.model.send_message import SendMessage
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
    api_instance = basicmessage_api.BasicmessageApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    body = SendMessage(
        content="Hello",
    ) # SendMessage |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a basic message to a connection
        api_response = api_instance.connections_conn_id_send_message_post(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BasicmessageApi->connections_conn_id_send_message_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a basic message to a connection
        api_response = api_instance.connections_conn_id_send_message_post(conn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BasicmessageApi->connections_conn_id_send_message_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **body** | [**SendMessage**](SendMessage.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

