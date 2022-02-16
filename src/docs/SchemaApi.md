# openapi_client.SchemaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schemas_created_get**](SchemaApi.md#schemas_created_get) | **GET** /schemas/created | Search for matching schema that agent originated
[**schemas_post**](SchemaApi.md#schemas_post) | **POST** /schemas | Sends a schema to the ledger
[**schemas_schema_id_get**](SchemaApi.md#schemas_schema_id_get) | **GET** /schemas/{schema_id} | Gets a schema from the ledger
[**schemas_schema_id_write_record_post**](SchemaApi.md#schemas_schema_id_write_record_post) | **POST** /schemas/{schema_id}/write_record | Writes a schema non-secret record to the wallet


# **schemas_created_get**
> SchemasCreatedResult schemas_created_get()

Search for matching schema that agent originated

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import schema_api
from openapi_client.model.schemas_created_result import SchemasCreatedResult
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
    api_instance = schema_api.SchemaApi(api_client)
    schema_id = "FZPn3BZqhoxS1o7RzixZRE:2:hJk C>i H'qT\{<?':11167.364560770849968420005670.06712463." # str | Schema identifier (optional)
    schema_issuer_did = "did:sov:ZPn3BZqhoxS1o7RzixZRE9" # str | Schema issuer DID (optional)
    schema_name = "schema_name_example" # str | Schema name (optional)
    schema_version = "1" # str | Schema version (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for matching schema that agent originated
        api_response = api_instance.schemas_created_get(schema_id=schema_id, schema_issuer_did=schema_issuer_did, schema_name=schema_name, schema_version=schema_version)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemaApi->schemas_created_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**| Schema identifier | [optional]
 **schema_issuer_did** | **str**| Schema issuer DID | [optional]
 **schema_name** | **str**| Schema name | [optional]
 **schema_version** | **str**| Schema version | [optional]

### Return type

[**SchemasCreatedResult**](SchemasCreatedResult.md)

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

# **schemas_post**
> TxnOrSchemaSendResult schemas_post()

Sends a schema to the ledger

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import schema_api
from openapi_client.model.txn_or_schema_send_result import TxnOrSchemaSendResult
from openapi_client.model.schema_send_request import SchemaSendRequest
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
    api_instance = schema_api.SchemaApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier (optional)
    create_transaction_for_endorser = True # bool | Create Transaction For Endorser's signature (optional)
    body = SchemaSendRequest(
        attributes=[
            "score",
        ],
        schema_name="prefs",
        schema_version="1.0",
    ) # SchemaSendRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a schema to the ledger
        api_response = api_instance.schemas_post(conn_id=conn_id, create_transaction_for_endorser=create_transaction_for_endorser, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemaApi->schemas_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | [optional]
 **create_transaction_for_endorser** | **bool**| Create Transaction For Endorser&#39;s signature | [optional]
 **body** | [**SchemaSendRequest**](SchemaSendRequest.md)|  | [optional]

### Return type

[**TxnOrSchemaSendResult**](TxnOrSchemaSendResult.md)

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

# **schemas_schema_id_get**
> SchemaGetResult schemas_schema_id_get(schema_id)

Gets a schema from the ledger

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import schema_api
from openapi_client.model.schema_get_result import SchemaGetResult
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
    api_instance = schema_api.SchemaApi(api_client)
    schema_id = "ZPn3BZqhoxS1o7RzixZRE9:2:Jk :902116926747211167.364560770849968420005670.06712463.29171.369815727963338434.8878.32524.20" # str | Schema identifier

    # example passing only required values which don't have defaults set
    try:
        # Gets a schema from the ledger
        api_response = api_instance.schemas_schema_id_get(schema_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemaApi->schemas_schema_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**| Schema identifier |

### Return type

[**SchemaGetResult**](SchemaGetResult.md)

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

# **schemas_schema_id_write_record_post**
> SchemaGetResult schemas_schema_id_write_record_post(schema_id)

Writes a schema non-secret record to the wallet

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import schema_api
from openapi_client.model.schema_get_result import SchemaGetResult
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
    api_instance = schema_api.SchemaApi(api_client)
    schema_id = "ZPn3BZqhoxS1o7RzixZRE9:2:Jk :902116926747211167.364560770849968420005670.06712463.29171.369815727963338434.8878.32524.20" # str | Schema identifier

    # example passing only required values which don't have defaults set
    try:
        # Writes a schema non-secret record to the wallet
        api_response = api_instance.schemas_schema_id_write_record_post(schema_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchemaApi->schemas_schema_id_write_record_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**| Schema identifier |

### Return type

[**SchemaGetResult**](SchemaGetResult.md)

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

