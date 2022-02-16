# openapi_client.JsonldApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jsonld_sign_post**](JsonldApi.md#jsonld_sign_post) | **POST** /jsonld/sign | Sign a JSON-LD structure and return it
[**jsonld_verify_post**](JsonldApi.md#jsonld_verify_post) | **POST** /jsonld/verify | Verify a JSON-LD structure.


# **jsonld_sign_post**
> SignResponse jsonld_sign_post()

Sign a JSON-LD structure and return it

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import jsonld_api
from openapi_client.model.sign_request import SignRequest
from openapi_client.model.sign_response import SignResponse
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
    api_instance = jsonld_api.JsonldApi(api_client)
    body = SignRequest(
        doc=Doc(
            credential={},
            options={},
        ),
        verkey="verkey_example",
    ) # SignRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sign a JSON-LD structure and return it
        api_response = api_instance.jsonld_sign_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JsonldApi->jsonld_sign_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignRequest**](SignRequest.md)|  | [optional]

### Return type

[**SignResponse**](SignResponse.md)

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

# **jsonld_verify_post**
> VerifyResponse jsonld_verify_post()

Verify a JSON-LD structure.

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import jsonld_api
from openapi_client.model.verify_request import VerifyRequest
from openapi_client.model.verify_response import VerifyResponse
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
    api_instance = jsonld_api.JsonldApi(api_client)
    body = VerifyRequest(
        doc={},
        verkey="verkey_example",
    ) # VerifyRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Verify a JSON-LD structure.
        api_response = api_instance.jsonld_verify_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JsonldApi->jsonld_verify_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyRequest**](VerifyRequest.md)|  | [optional]

### Return type

[**VerifyResponse**](VerifyResponse.md)

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

