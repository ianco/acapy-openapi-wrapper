# openapi_client.MultitenancyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**multitenancy_wallet_post**](MultitenancyApi.md#multitenancy_wallet_post) | **POST** /multitenancy/wallet | Create a subwallet
[**multitenancy_wallet_wallet_id_get**](MultitenancyApi.md#multitenancy_wallet_wallet_id_get) | **GET** /multitenancy/wallet/{wallet_id} | Get a single subwallet
[**multitenancy_wallet_wallet_id_put**](MultitenancyApi.md#multitenancy_wallet_wallet_id_put) | **PUT** /multitenancy/wallet/{wallet_id} | Update a subwallet
[**multitenancy_wallet_wallet_id_remove_post**](MultitenancyApi.md#multitenancy_wallet_wallet_id_remove_post) | **POST** /multitenancy/wallet/{wallet_id}/remove | Remove a subwallet
[**multitenancy_wallet_wallet_id_token_post**](MultitenancyApi.md#multitenancy_wallet_wallet_id_token_post) | **POST** /multitenancy/wallet/{wallet_id}/token | Get auth token for a subwallet
[**multitenancy_wallets_get**](MultitenancyApi.md#multitenancy_wallets_get) | **GET** /multitenancy/wallets | Query subwallets


# **multitenancy_wallet_post**
> CreateWalletResponse multitenancy_wallet_post()

Create a subwallet

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import multitenancy_api
from openapi_client.model.create_wallet_request import CreateWalletRequest
from openapi_client.model.create_wallet_response import CreateWalletResponse
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
    api_instance = multitenancy_api.MultitenancyApi(api_client)
    body = CreateWalletRequest(
        image_url="https://aries.ca/images/sample.png",
        key_management_mode="managed",
        label="Alice",
        wallet_dispatch_type="default",
        wallet_key="MySecretKey123",
        wallet_name="MyNewWallet",
        wallet_type="indy",
        wallet_webhook_urls=[
            "http://localhost:8022/webhooks",
        ],
    ) # CreateWalletRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a subwallet
        api_response = api_instance.multitenancy_wallet_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenancyApi->multitenancy_wallet_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWalletRequest**](CreateWalletRequest.md)|  | [optional]

### Return type

[**CreateWalletResponse**](CreateWalletResponse.md)

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

# **multitenancy_wallet_wallet_id_get**
> WalletRecord multitenancy_wallet_wallet_id_get(wallet_id)

Get a single subwallet

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import multitenancy_api
from openapi_client.model.wallet_record import WalletRecord
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
    api_instance = multitenancy_api.MultitenancyApi(api_client)
    wallet_id = "wallet_id_example" # str | Subwallet identifier

    # example passing only required values which don't have defaults set
    try:
        # Get a single subwallet
        api_response = api_instance.multitenancy_wallet_wallet_id_get(wallet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenancyApi->multitenancy_wallet_wallet_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Subwallet identifier |

### Return type

[**WalletRecord**](WalletRecord.md)

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

# **multitenancy_wallet_wallet_id_put**
> WalletRecord multitenancy_wallet_wallet_id_put(wallet_id)

Update a subwallet

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import multitenancy_api
from openapi_client.model.update_wallet_request import UpdateWalletRequest
from openapi_client.model.wallet_record import WalletRecord
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
    api_instance = multitenancy_api.MultitenancyApi(api_client)
    wallet_id = "wallet_id_example" # str | Subwallet identifier
    body = UpdateWalletRequest(
        image_url="https://aries.ca/images/sample.png",
        label="Alice",
        wallet_dispatch_type="default",
        wallet_webhook_urls=[
            "http://localhost:8022/webhooks",
        ],
    ) # UpdateWalletRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a subwallet
        api_response = api_instance.multitenancy_wallet_wallet_id_put(wallet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenancyApi->multitenancy_wallet_wallet_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a subwallet
        api_response = api_instance.multitenancy_wallet_wallet_id_put(wallet_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenancyApi->multitenancy_wallet_wallet_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Subwallet identifier |
 **body** | [**UpdateWalletRequest**](UpdateWalletRequest.md)|  | [optional]

### Return type

[**WalletRecord**](WalletRecord.md)

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

# **multitenancy_wallet_wallet_id_remove_post**
> bool, date, datetime, dict, float, int, list, str, none_type multitenancy_wallet_wallet_id_remove_post(wallet_id)

Remove a subwallet

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import multitenancy_api
from openapi_client.model.remove_wallet_request import RemoveWalletRequest
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
    api_instance = multitenancy_api.MultitenancyApi(api_client)
    wallet_id = "wallet_id_example" # str | Subwallet identifier
    body = RemoveWalletRequest(
        wallet_key="MySecretKey123",
    ) # RemoveWalletRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a subwallet
        api_response = api_instance.multitenancy_wallet_wallet_id_remove_post(wallet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenancyApi->multitenancy_wallet_wallet_id_remove_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a subwallet
        api_response = api_instance.multitenancy_wallet_wallet_id_remove_post(wallet_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenancyApi->multitenancy_wallet_wallet_id_remove_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Subwallet identifier |
 **body** | [**RemoveWalletRequest**](RemoveWalletRequest.md)|  | [optional]

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

# **multitenancy_wallet_wallet_id_token_post**
> CreateWalletTokenResponse multitenancy_wallet_wallet_id_token_post(wallet_id)

Get auth token for a subwallet

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import multitenancy_api
from openapi_client.model.create_wallet_token_request import CreateWalletTokenRequest
from openapi_client.model.create_wallet_token_response import CreateWalletTokenResponse
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
    api_instance = multitenancy_api.MultitenancyApi(api_client)
    wallet_id = "wallet_id_example" # str | 
    body = CreateWalletTokenRequest(
        wallet_key="MySecretKey123",
    ) # CreateWalletTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get auth token for a subwallet
        api_response = api_instance.multitenancy_wallet_wallet_id_token_post(wallet_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenancyApi->multitenancy_wallet_wallet_id_token_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get auth token for a subwallet
        api_response = api_instance.multitenancy_wallet_wallet_id_token_post(wallet_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenancyApi->multitenancy_wallet_wallet_id_token_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  |
 **body** | [**CreateWalletTokenRequest**](CreateWalletTokenRequest.md)|  | [optional]

### Return type

[**CreateWalletTokenResponse**](CreateWalletTokenResponse.md)

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

# **multitenancy_wallets_get**
> WalletList multitenancy_wallets_get()

Query subwallets

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import multitenancy_api
from openapi_client.model.wallet_list import WalletList
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
    api_instance = multitenancy_api.MultitenancyApi(api_client)
    wallet_name = "wallet_name_example" # str | Wallet name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query subwallets
        api_response = api_instance.multitenancy_wallets_get(wallet_name=wallet_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MultitenancyApi->multitenancy_wallets_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_name** | **str**| Wallet name | [optional]

### Return type

[**WalletList**](WalletList.md)

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

