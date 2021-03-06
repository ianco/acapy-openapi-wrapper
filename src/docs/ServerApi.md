# openapi_client.ServerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**features_get**](ServerApi.md#features_get) | **GET** /features | Query supported features
[**plugins_get**](ServerApi.md#plugins_get) | **GET** /plugins | Fetch the list of loaded plugins
[**shutdown_get**](ServerApi.md#shutdown_get) | **GET** /shutdown | Shut down server
[**status_config_get**](ServerApi.md#status_config_get) | **GET** /status/config | Fetch the server configuration
[**status_get**](ServerApi.md#status_get) | **GET** /status | Fetch the server status
[**status_live_get**](ServerApi.md#status_live_get) | **GET** /status/live | Liveliness check
[**status_ready_get**](ServerApi.md#status_ready_get) | **GET** /status/ready | Readiness check
[**status_reset_post**](ServerApi.md#status_reset_post) | **POST** /status/reset | Reset statistics


# **features_get**
> QueryResult features_get()

Query supported features

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.query_result import QueryResult
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
    api_instance = server_api.ServerApi(api_client)
    query = "query_example" # str | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query supported features
        api_response = api_instance.features_get(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->features_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query | [optional]

### Return type

[**QueryResult**](QueryResult.md)

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

# **plugins_get**
> AdminModules plugins_get()

Fetch the list of loaded plugins

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.admin_modules import AdminModules
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
    api_instance = server_api.ServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch the list of loaded plugins
        api_response = api_instance.plugins_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->plugins_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminModules**](AdminModules.md)

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

# **shutdown_get**
> bool, date, datetime, dict, float, int, list, str, none_type shutdown_get()

Shut down server

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import server_api
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
    api_instance = server_api.ServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Shut down server
        api_response = api_instance.shutdown_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->shutdown_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **status_config_get**
> AdminConfig status_config_get()

Fetch the server configuration

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.admin_config import AdminConfig
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
    api_instance = server_api.ServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch the server configuration
        api_response = api_instance.status_config_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->status_config_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminConfig**](AdminConfig.md)

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

# **status_get**
> AdminStatus status_get()

Fetch the server status

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.admin_status import AdminStatus
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
    api_instance = server_api.ServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch the server status
        api_response = api_instance.status_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->status_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminStatus**](AdminStatus.md)

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

# **status_live_get**
> AdminStatusLiveliness status_live_get()

Liveliness check

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.admin_status_liveliness import AdminStatusLiveliness
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
    api_instance = server_api.ServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liveliness check
        api_response = api_instance.status_live_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->status_live_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminStatusLiveliness**](AdminStatusLiveliness.md)

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

# **status_ready_get**
> AdminStatusReadiness status_ready_get()

Readiness check

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import server_api
from openapi_client.model.admin_status_readiness import AdminStatusReadiness
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
    api_instance = server_api.ServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Readiness check
        api_response = api_instance.status_ready_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->status_ready_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminStatusReadiness**](AdminStatusReadiness.md)

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

# **status_reset_post**
> bool, date, datetime, dict, float, int, list, str, none_type status_reset_post()

Reset statistics

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import server_api
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
    api_instance = server_api.ServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Reset statistics
        api_response = api_instance.status_reset_post()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServerApi->status_reset_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

