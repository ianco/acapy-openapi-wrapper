# openapi_client.CredentialDefinitionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credential_definitions_created_get**](CredentialDefinitionApi.md#credential_definitions_created_get) | **GET** /credential-definitions/created | Search for matching credential definitions that agent originated
[**credential_definitions_cred_def_id_get**](CredentialDefinitionApi.md#credential_definitions_cred_def_id_get) | **GET** /credential-definitions/{cred_def_id} | Gets a credential definition from the ledger
[**credential_definitions_cred_def_id_write_record_post**](CredentialDefinitionApi.md#credential_definitions_cred_def_id_write_record_post) | **POST** /credential-definitions/{cred_def_id}/write_record | Writes a credential definition non-secret record to the wallet
[**credential_definitions_post**](CredentialDefinitionApi.md#credential_definitions_post) | **POST** /credential-definitions | Sends a credential definition to the ledger


# **credential_definitions_created_get**
> CredentialDefinitionsCreatedResult credential_definitions_created_get()

Search for matching credential definitions that agent originated

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import credential_definition_api
from openapi_client.model.credential_definitions_created_result import CredentialDefinitionsCreatedResult
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
    api_instance = credential_definition_api.CredentialDefinitionApi(api_client)
    cred_def_id = "FZPn3BZqhoxS1o7RzixZRE:3:CL:85500850762068629339333975:ag2/!K" # str | Credential definition id (optional)
    issuer_did = "did:sov:ZPn3BZqhoxS1o7RzixZRE9" # str | Issuer DID (optional)
    schema_id = "FZPn3BZqhoxS1o7RzixZRE:2:hJk C>i H'qT\{<?':11167.364560770849968420005670.06712463." # str | Schema identifier (optional)
    schema_issuer_did = "did:sov:ZPn3BZqhoxS1o7RzixZRE9" # str | Schema issuer DID (optional)
    schema_name = "schema_name_example" # str | Schema name (optional)
    schema_version = "1" # str | Schema version (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for matching credential definitions that agent originated
        api_response = api_instance.credential_definitions_created_get(cred_def_id=cred_def_id, issuer_did=issuer_did, schema_id=schema_id, schema_issuer_did=schema_issuer_did, schema_name=schema_name, schema_version=schema_version)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CredentialDefinitionApi->credential_definitions_created_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition id | [optional]
 **issuer_did** | **str**| Issuer DID | [optional]
 **schema_id** | **str**| Schema identifier | [optional]
 **schema_issuer_did** | **str**| Schema issuer DID | [optional]
 **schema_name** | **str**| Schema name | [optional]
 **schema_version** | **str**| Schema version | [optional]

### Return type

[**CredentialDefinitionsCreatedResult**](CredentialDefinitionsCreatedResult.md)

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

# **credential_definitions_cred_def_id_get**
> CredentialDefinitionGetResult credential_definitions_cred_def_id_get(cred_def_id)

Gets a credential definition from the ledger

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import credential_definition_api
from openapi_client.model.credential_definition_get_result import CredentialDefinitionGetResult
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
    api_instance = credential_definition_api.CredentialDefinitionApi(api_client)
    cred_def_id = "FZPn3BZqhoxS1o7RzixZRE:3:CL:85500850762068629339333975:ag2/!K" # str | Credential definition identifier

    # example passing only required values which don't have defaults set
    try:
        # Gets a credential definition from the ledger
        api_response = api_instance.credential_definitions_cred_def_id_get(cred_def_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CredentialDefinitionApi->credential_definitions_cred_def_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition identifier |

### Return type

[**CredentialDefinitionGetResult**](CredentialDefinitionGetResult.md)

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

# **credential_definitions_cred_def_id_write_record_post**
> CredentialDefinitionGetResult credential_definitions_cred_def_id_write_record_post(cred_def_id)

Writes a credential definition non-secret record to the wallet

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import credential_definition_api
from openapi_client.model.credential_definition_get_result import CredentialDefinitionGetResult
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
    api_instance = credential_definition_api.CredentialDefinitionApi(api_client)
    cred_def_id = "FZPn3BZqhoxS1o7RzixZRE:3:CL:85500850762068629339333975:ag2/!K" # str | Credential definition identifier

    # example passing only required values which don't have defaults set
    try:
        # Writes a credential definition non-secret record to the wallet
        api_response = api_instance.credential_definitions_cred_def_id_write_record_post(cred_def_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CredentialDefinitionApi->credential_definitions_cred_def_id_write_record_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_def_id** | **str**| Credential definition identifier |

### Return type

[**CredentialDefinitionGetResult**](CredentialDefinitionGetResult.md)

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

# **credential_definitions_post**
> TxnOrCredentialDefinitionSendResult credential_definitions_post()

Sends a credential definition to the ledger

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import credential_definition_api
from openapi_client.model.txn_or_credential_definition_send_result import TxnOrCredentialDefinitionSendResult
from openapi_client.model.credential_definition_send_request import CredentialDefinitionSendRequest
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
    api_instance = credential_definition_api.CredentialDefinitionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier (optional)
    create_transaction_for_endorser = True # bool | Create Transaction For Endorser's signature (optional)
    body = CredentialDefinitionSendRequest(
        revocation_registry_size=1000,
        schema_id="WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0",
        support_revocation=True,
        tag="default",
    ) # CredentialDefinitionSendRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a credential definition to the ledger
        api_response = api_instance.credential_definitions_post(conn_id=conn_id, create_transaction_for_endorser=create_transaction_for_endorser, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CredentialDefinitionApi->credential_definitions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier | [optional]
 **create_transaction_for_endorser** | **bool**| Create Transaction For Endorser&#39;s signature | [optional]
 **body** | [**CredentialDefinitionSendRequest**](CredentialDefinitionSendRequest.md)|  | [optional]

### Return type

[**TxnOrCredentialDefinitionSendResult**](TxnOrCredentialDefinitionSendResult.md)

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

