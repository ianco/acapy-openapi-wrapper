# openapi_client.EndorseTransactionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transaction_tran_id_resend_post**](EndorseTransactionApi.md#transaction_tran_id_resend_post) | **POST** /transaction/{tran_id}/resend | For Author to resend a particular transaction request
[**transactions_conn_id_set_endorser_info_post**](EndorseTransactionApi.md#transactions_conn_id_set_endorser_info_post) | **POST** /transactions/{conn_id}/set-endorser-info | Set Endorser Info
[**transactions_conn_id_set_endorser_role_post**](EndorseTransactionApi.md#transactions_conn_id_set_endorser_role_post) | **POST** /transactions/{conn_id}/set-endorser-role | Set transaction jobs
[**transactions_create_request_post**](EndorseTransactionApi.md#transactions_create_request_post) | **POST** /transactions/create-request | For author to send a transaction request
[**transactions_get**](EndorseTransactionApi.md#transactions_get) | **GET** /transactions | Query transactions
[**transactions_tran_id_cancel_post**](EndorseTransactionApi.md#transactions_tran_id_cancel_post) | **POST** /transactions/{tran_id}/cancel | For Author to cancel a particular transaction request
[**transactions_tran_id_endorse_post**](EndorseTransactionApi.md#transactions_tran_id_endorse_post) | **POST** /transactions/{tran_id}/endorse | For Endorser to endorse a particular transaction record
[**transactions_tran_id_get**](EndorseTransactionApi.md#transactions_tran_id_get) | **GET** /transactions/{tran_id} | Fetch a single transaction record
[**transactions_tran_id_refuse_post**](EndorseTransactionApi.md#transactions_tran_id_refuse_post) | **POST** /transactions/{tran_id}/refuse | For Endorser to refuse a particular transaction record
[**transactions_tran_id_write_post**](EndorseTransactionApi.md#transactions_tran_id_write_post) | **POST** /transactions/{tran_id}/write | For Author / Endorser to write an endorsed transaction to the ledger


# **transaction_tran_id_resend_post**
> TransactionRecord transaction_tran_id_resend_post(tran_id)

For Author to resend a particular transaction request

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import endorse_transaction_api
from openapi_client.model.transaction_record import TransactionRecord
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
    api_instance = endorse_transaction_api.EndorseTransactionApi(api_client)
    tran_id = "tran_id_example" # str | Transaction identifier

    # example passing only required values which don't have defaults set
    try:
        # For Author to resend a particular transaction request
        api_response = api_instance.transaction_tran_id_resend_post(tran_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transaction_tran_id_resend_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Transaction identifier |

### Return type

[**TransactionRecord**](TransactionRecord.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_conn_id_set_endorser_info_post**
> EndorserInfo transactions_conn_id_set_endorser_info_post(conn_id, endorser_did)

Set Endorser Info

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import endorse_transaction_api
from openapi_client.model.endorser_info import EndorserInfo
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
    api_instance = endorse_transaction_api.EndorseTransactionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    endorser_did = "endorser_did_example" # str | Endorser DID
    endorser_name = "endorser_name_example" # str | Endorser Name (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set Endorser Info
        api_response = api_instance.transactions_conn_id_set_endorser_info_post(conn_id, endorser_did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_conn_id_set_endorser_info_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set Endorser Info
        api_response = api_instance.transactions_conn_id_set_endorser_info_post(conn_id, endorser_did, endorser_name=endorser_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_conn_id_set_endorser_info_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **endorser_did** | **str**| Endorser DID |
 **endorser_name** | **str**| Endorser Name | [optional]

### Return type

[**EndorserInfo**](EndorserInfo.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_conn_id_set_endorser_role_post**
> TransactionJobs transactions_conn_id_set_endorser_role_post(conn_id)

Set transaction jobs

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import endorse_transaction_api
from openapi_client.model.transaction_jobs import TransactionJobs
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
    api_instance = endorse_transaction_api.EndorseTransactionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    transaction_my_job = "TRANSACTION_AUTHOR" # str | Transaction related jobs (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set transaction jobs
        api_response = api_instance.transactions_conn_id_set_endorser_role_post(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_conn_id_set_endorser_role_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set transaction jobs
        api_response = api_instance.transactions_conn_id_set_endorser_role_post(conn_id, transaction_my_job=transaction_my_job)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_conn_id_set_endorser_role_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **transaction_my_job** | **str**| Transaction related jobs | [optional]

### Return type

[**TransactionJobs**](TransactionJobs.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_create_request_post**
> TransactionRecord transactions_create_request_post(tran_id)

For author to send a transaction request

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import endorse_transaction_api
from openapi_client.model.transaction_record import TransactionRecord
from openapi_client.model.date import Date
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
    api_instance = endorse_transaction_api.EndorseTransactionApi(api_client)
    tran_id = "tran_id_example" # str | Transaction identifier
    endorser_write_txn = True # bool | Endorser will write the transaction after endorsing it (optional)
    body = Date(
        expires_time=dateutil_parser('2021-03-29T05:22:19Z'),
    ) # Date |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # For author to send a transaction request
        api_response = api_instance.transactions_create_request_post(tran_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_create_request_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # For author to send a transaction request
        api_response = api_instance.transactions_create_request_post(tran_id, endorser_write_txn=endorser_write_txn, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_create_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Transaction identifier |
 **endorser_write_txn** | **bool**| Endorser will write the transaction after endorsing it | [optional]
 **body** | [**Date**](Date.md)|  | [optional]

### Return type

[**TransactionRecord**](TransactionRecord.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_get**
> TransactionList transactions_get()

Query transactions

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import endorse_transaction_api
from openapi_client.model.transaction_list import TransactionList
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
    api_instance = endorse_transaction_api.EndorseTransactionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Query transactions
        api_response = api_instance.transactions_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TransactionList**](TransactionList.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_tran_id_cancel_post**
> TransactionRecord transactions_tran_id_cancel_post(tran_id)

For Author to cancel a particular transaction request

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import endorse_transaction_api
from openapi_client.model.transaction_record import TransactionRecord
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
    api_instance = endorse_transaction_api.EndorseTransactionApi(api_client)
    tran_id = "tran_id_example" # str | Transaction identifier

    # example passing only required values which don't have defaults set
    try:
        # For Author to cancel a particular transaction request
        api_response = api_instance.transactions_tran_id_cancel_post(tran_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_tran_id_cancel_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Transaction identifier |

### Return type

[**TransactionRecord**](TransactionRecord.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_tran_id_endorse_post**
> TransactionRecord transactions_tran_id_endorse_post(tran_id)

For Endorser to endorse a particular transaction record

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import endorse_transaction_api
from openapi_client.model.transaction_record import TransactionRecord
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
    api_instance = endorse_transaction_api.EndorseTransactionApi(api_client)
    tran_id = "tran_id_example" # str | Transaction identifier

    # example passing only required values which don't have defaults set
    try:
        # For Endorser to endorse a particular transaction record
        api_response = api_instance.transactions_tran_id_endorse_post(tran_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_tran_id_endorse_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Transaction identifier |

### Return type

[**TransactionRecord**](TransactionRecord.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_tran_id_get**
> TransactionRecord transactions_tran_id_get(tran_id)

Fetch a single transaction record

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import endorse_transaction_api
from openapi_client.model.transaction_record import TransactionRecord
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
    api_instance = endorse_transaction_api.EndorseTransactionApi(api_client)
    tran_id = "tran_id_example" # str | Transaction identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch a single transaction record
        api_response = api_instance.transactions_tran_id_get(tran_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_tran_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Transaction identifier |

### Return type

[**TransactionRecord**](TransactionRecord.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_tran_id_refuse_post**
> TransactionRecord transactions_tran_id_refuse_post(tran_id)

For Endorser to refuse a particular transaction record

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import endorse_transaction_api
from openapi_client.model.transaction_record import TransactionRecord
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
    api_instance = endorse_transaction_api.EndorseTransactionApi(api_client)
    tran_id = "tran_id_example" # str | Transaction identifier

    # example passing only required values which don't have defaults set
    try:
        # For Endorser to refuse a particular transaction record
        api_response = api_instance.transactions_tran_id_refuse_post(tran_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_tran_id_refuse_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Transaction identifier |

### Return type

[**TransactionRecord**](TransactionRecord.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_tran_id_write_post**
> TransactionRecord transactions_tran_id_write_post(tran_id)

For Author / Endorser to write an endorsed transaction to the ledger

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import endorse_transaction_api
from openapi_client.model.transaction_record import TransactionRecord
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
    api_instance = endorse_transaction_api.EndorseTransactionApi(api_client)
    tran_id = "tran_id_example" # str | Transaction identifier

    # example passing only required values which don't have defaults set
    try:
        # For Author / Endorser to write an endorsed transaction to the ledger
        api_response = api_instance.transactions_tran_id_write_post(tran_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EndorseTransactionApi->transactions_tran_id_write_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Transaction identifier |

### Return type

[**TransactionRecord**](TransactionRecord.md)

### Authorization

[AuthorizationHeader](../README.md#AuthorizationHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

