# openapi_client.WalletApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_did_create_post**](WalletApi.md#wallet_did_create_post) | **POST** /wallet/did/create | Create a local DID
[**wallet_did_get**](WalletApi.md#wallet_did_get) | **GET** /wallet/did | List wallet DIDs
[**wallet_did_local_rotate_keypair_patch**](WalletApi.md#wallet_did_local_rotate_keypair_patch) | **PATCH** /wallet/did/local/rotate-keypair | Rotate keypair for a DID not posted to the ledger
[**wallet_did_public_get**](WalletApi.md#wallet_did_public_get) | **GET** /wallet/did/public | Fetch the current public DID
[**wallet_did_public_post**](WalletApi.md#wallet_did_public_post) | **POST** /wallet/did/public | Assign the current public DID
[**wallet_get_did_endpoint_get**](WalletApi.md#wallet_get_did_endpoint_get) | **GET** /wallet/get-did-endpoint | Query DID endpoint in wallet
[**wallet_set_did_endpoint_post**](WalletApi.md#wallet_set_did_endpoint_post) | **POST** /wallet/set-did-endpoint | Update endpoint in wallet and on ledger if posted to it


# **wallet_did_create_post**
> DIDResult wallet_did_create_post()

Create a local DID

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import wallet_api
from openapi_client.model.did_create import DIDCreate
from openapi_client.model.did_result import DIDResult
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
    api_instance = wallet_api.WalletApi(api_client)
    body = DIDCreate(
        method="sov",
        options={},
    ) # DIDCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a local DID
        api_response = api_instance.wallet_did_create_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletApi->wallet_did_create_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DIDCreate**](DIDCreate.md)|  | [optional]

### Return type

[**DIDResult**](DIDResult.md)

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

# **wallet_did_get**
> DIDList wallet_did_get()

List wallet DIDs

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import wallet_api
from openapi_client.model.did_list import DIDList
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
    api_instance = wallet_api.WalletApi(api_client)
    did = "did:sov:Pn3BZqhoxS1o7RzixZRE9" # str | DID of interest (optional)
    key_type = "ed25519" # str | Key type to query for. (optional)
    method = "key" # str | DID method to query for. e.g. sov to only fetch indy/sov DIDs (optional)
    posture = "public" # str | Whether DID is current public DID, posted to ledger but current public DID, or local to the wallet (optional)
    verkey = "FZPn3BZqhoxS1o7RzixZRE9TRJrjhKGPim39DqZKtY2C" # str | Verification key of interest (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List wallet DIDs
        api_response = api_instance.wallet_did_get(did=did, key_type=key_type, method=method, posture=posture, verkey=verkey)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletApi->wallet_did_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest | [optional]
 **key_type** | **str**| Key type to query for. | [optional]
 **method** | **str**| DID method to query for. e.g. sov to only fetch indy/sov DIDs | [optional]
 **posture** | **str**| Whether DID is current public DID, posted to ledger but current public DID, or local to the wallet | [optional]
 **verkey** | **str**| Verification key of interest | [optional]

### Return type

[**DIDList**](DIDList.md)

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

# **wallet_did_local_rotate_keypair_patch**
> bool, date, datetime, dict, float, int, list, str, none_type wallet_did_local_rotate_keypair_patch(did)

Rotate keypair for a DID not posted to the ledger

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import wallet_api
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
    api_instance = wallet_api.WalletApi(api_client)
    did = "did:sov:ZPn3BZqhoxS1o7RzixZRE9" # str | DID of interest

    # example passing only required values which don't have defaults set
    try:
        # Rotate keypair for a DID not posted to the ledger
        api_response = api_instance.wallet_did_local_rotate_keypair_patch(did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletApi->wallet_did_local_rotate_keypair_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest |

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

# **wallet_did_public_get**
> DIDResult wallet_did_public_get()

Fetch the current public DID

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import wallet_api
from openapi_client.model.did_result import DIDResult
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
    api_instance = wallet_api.WalletApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch the current public DID
        api_response = api_instance.wallet_did_public_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletApi->wallet_did_public_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DIDResult**](DIDResult.md)

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

# **wallet_did_public_post**
> DIDResult wallet_did_public_post(did)

Assign the current public DID

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import wallet_api
from openapi_client.model.did_result import DIDResult
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
    api_instance = wallet_api.WalletApi(api_client)
    did = "did:sov:ZPn3BZqhoxS1o7RzixZRE9" # str | DID of interest

    # example passing only required values which don't have defaults set
    try:
        # Assign the current public DID
        api_response = api_instance.wallet_did_public_post(did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletApi->wallet_did_public_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest |

### Return type

[**DIDResult**](DIDResult.md)

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

# **wallet_get_did_endpoint_get**
> DIDEndpoint wallet_get_did_endpoint_get(did)

Query DID endpoint in wallet

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import wallet_api
from openapi_client.model.did_endpoint import DIDEndpoint
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
    api_instance = wallet_api.WalletApi(api_client)
    did = "did:sov:ZPn3BZqhoxS1o7RzixZRE9" # str | DID of interest

    # example passing only required values which don't have defaults set
    try:
        # Query DID endpoint in wallet
        api_response = api_instance.wallet_get_did_endpoint_get(did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletApi->wallet_get_did_endpoint_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID of interest |

### Return type

[**DIDEndpoint**](DIDEndpoint.md)

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

# **wallet_set_did_endpoint_post**
> bool, date, datetime, dict, float, int, list, str, none_type wallet_set_did_endpoint_post()

Update endpoint in wallet and on ledger if posted to it

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import wallet_api
from openapi_client.model.did_endpoint_with_type import DIDEndpointWithType
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
    api_instance = wallet_api.WalletApi(api_client)
    body = DIDEndpointWithType(
        did="WgWxqztrNooG92RXvxSTWv",
        endpoint="https://myhost:8021",
        endpoint_type="Endpoint",
    ) # DIDEndpointWithType |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update endpoint in wallet and on ledger if posted to it
        api_response = api_instance.wallet_set_did_endpoint_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletApi->wallet_set_did_endpoint_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DIDEndpointWithType**](DIDEndpointWithType.md)|  | [optional]

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

