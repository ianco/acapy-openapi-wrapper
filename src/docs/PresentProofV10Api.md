# openapi_client.PresentProofV10Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**present_proof_create_request_post**](PresentProofV10Api.md#present_proof_create_request_post) | **POST** /present-proof/create-request | Creates a presentation request not bound to any proposal or connection
[**present_proof_records_get**](PresentProofV10Api.md#present_proof_records_get) | **GET** /present-proof/records | Fetch all present-proof exchange records
[**present_proof_records_pres_ex_id_credentials_get**](PresentProofV10Api.md#present_proof_records_pres_ex_id_credentials_get) | **GET** /present-proof/records/{pres_ex_id}/credentials | Fetch credentials for a presentation request from wallet
[**present_proof_records_pres_ex_id_delete**](PresentProofV10Api.md#present_proof_records_pres_ex_id_delete) | **DELETE** /present-proof/records/{pres_ex_id} | Remove an existing presentation exchange record
[**present_proof_records_pres_ex_id_get**](PresentProofV10Api.md#present_proof_records_pres_ex_id_get) | **GET** /present-proof/records/{pres_ex_id} | Fetch a single presentation exchange record
[**present_proof_records_pres_ex_id_problem_report_post**](PresentProofV10Api.md#present_proof_records_pres_ex_id_problem_report_post) | **POST** /present-proof/records/{pres_ex_id}/problem-report | Send a problem report for presentation exchange
[**present_proof_records_pres_ex_id_send_presentation_post**](PresentProofV10Api.md#present_proof_records_pres_ex_id_send_presentation_post) | **POST** /present-proof/records/{pres_ex_id}/send-presentation | Sends a proof presentation
[**present_proof_records_pres_ex_id_send_request_post**](PresentProofV10Api.md#present_proof_records_pres_ex_id_send_request_post) | **POST** /present-proof/records/{pres_ex_id}/send-request | Sends a presentation request in reference to a proposal
[**present_proof_records_pres_ex_id_verify_presentation_post**](PresentProofV10Api.md#present_proof_records_pres_ex_id_verify_presentation_post) | **POST** /present-proof/records/{pres_ex_id}/verify-presentation | Verify a received presentation
[**present_proof_send_proposal_post**](PresentProofV10Api.md#present_proof_send_proposal_post) | **POST** /present-proof/send-proposal | Sends a presentation proposal
[**present_proof_send_request_post**](PresentProofV10Api.md#present_proof_send_request_post) | **POST** /present-proof/send-request | Sends a free presentation request not bound to any proposal


# **present_proof_create_request_post**
> V10PresentationExchange present_proof_create_request_post()

Creates a presentation request not bound to any proposal or connection

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
from openapi_client.model.v10_presentation_exchange import V10PresentationExchange
from openapi_client.model.v10_presentation_create_request_request import V10PresentationCreateRequestRequest
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    body = V10PresentationCreateRequestRequest(
        comment="comment_example",
        proof_request=IndyProofRequest(
            name="Proof request",
            non_revoked={},
            nonce="1",
            requested_attributes={
                "key": IndyProofReqAttrSpec(
                    name="favouriteDrink",
                    names=[
                        "age",
                    ],
                    non_revoked={},
                    restrictions=[
                        {
                            "key": "WgWxqztrNooG92RXvxSTWv:3:CL:20:tag",
                        },
                    ],
                ),
            },
            requested_predicates={
                "key": IndyProofReqPredSpec(
                    name="index",
                    non_revoked={},
                    p_type=">=",
                    p_value=1,
                    restrictions=[
                        {
                            "key": "WgWxqztrNooG92RXvxSTWv:3:CL:20:tag",
                        },
                    ],
                ),
            },
            version="1.0",
        ),
        trace=False,
    ) # V10PresentationCreateRequestRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a presentation request not bound to any proposal or connection
        api_response = api_instance.present_proof_create_request_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_create_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10PresentationCreateRequestRequest**](V10PresentationCreateRequestRequest.md)|  | [optional]

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_records_get**
> V10PresentationExchangeList present_proof_records_get()

Fetch all present-proof exchange records

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
from openapi_client.model.v10_presentation_exchange_list import V10PresentationExchangeList
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    connection_id = "connection_id_example" # str | Connection identifier (optional)
    role = "prover" # str | Role assigned in presentation exchange (optional)
    state = "proposal_sent" # str | Presentation exchange state (optional)
    thread_id = "thread_id_example" # str | Thread identifier (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all present-proof exchange records
        api_response = api_instance.present_proof_records_get(connection_id=connection_id, role=role, state=state, thread_id=thread_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection identifier | [optional]
 **role** | **str**| Role assigned in presentation exchange | [optional]
 **state** | **str**| Presentation exchange state | [optional]
 **thread_id** | **str**| Thread identifier | [optional]

### Return type

[**V10PresentationExchangeList**](V10PresentationExchangeList.md)

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

# **present_proof_records_pres_ex_id_credentials_get**
> [IndyCredPrecis] present_proof_records_pres_ex_id_credentials_get(pres_ex_id)

Fetch credentials for a presentation request from wallet

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
from openapi_client.model.indy_cred_precis import IndyCredPrecis
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier
    count = "68072888001528021798096225500" # str | Maximum number to retrieve (optional)
    extra_query = "extra_query_example" # str | (JSON) object mapping referents to extra WQL queries (optional)
    referent = "referent_example" # str | Proof request referents of interest, comma-separated (optional)
    start = "4807288800152802179809" # str | Start index (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch credentials for a presentation request from wallet
        api_response = api_instance.present_proof_records_pres_ex_id_credentials_get(pres_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_credentials_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch credentials for a presentation request from wallet
        api_response = api_instance.present_proof_records_pres_ex_id_credentials_get(pres_ex_id, count=count, extra_query=extra_query, referent=referent, start=start)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_credentials_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |
 **count** | **str**| Maximum number to retrieve | [optional]
 **extra_query** | **str**| (JSON) object mapping referents to extra WQL queries | [optional]
 **referent** | **str**| Proof request referents of interest, comma-separated | [optional]
 **start** | **str**| Start index | [optional]

### Return type

[**[IndyCredPrecis]**](IndyCredPrecis.md)

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

# **present_proof_records_pres_ex_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type present_proof_records_pres_ex_id_delete(pres_ex_id)

Remove an existing presentation exchange record

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove an existing presentation exchange record
        api_response = api_instance.present_proof_records_pres_ex_id_delete(pres_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |

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

# **present_proof_records_pres_ex_id_get**
> V10PresentationExchange present_proof_records_pres_ex_id_get(pres_ex_id)

Fetch a single presentation exchange record

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
from openapi_client.model.v10_presentation_exchange import V10PresentationExchange
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch a single presentation exchange record
        api_response = api_instance.present_proof_records_pres_ex_id_get(pres_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_records_pres_ex_id_problem_report_post**
> bool, date, datetime, dict, float, int, list, str, none_type present_proof_records_pres_ex_id_problem_report_post(pres_ex_id)

Send a problem report for presentation exchange

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
from openapi_client.model.v10_presentation_problem_report_request import V10PresentationProblemReportRequest
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier
    body = V10PresentationProblemReportRequest(
        description="description_example",
    ) # V10PresentationProblemReportRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a problem report for presentation exchange
        api_response = api_instance.present_proof_records_pres_ex_id_problem_report_post(pres_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_problem_report_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a problem report for presentation exchange
        api_response = api_instance.present_proof_records_pres_ex_id_problem_report_post(pres_ex_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_problem_report_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |
 **body** | [**V10PresentationProblemReportRequest**](V10PresentationProblemReportRequest.md)|  | [optional]

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

# **present_proof_records_pres_ex_id_send_presentation_post**
> V10PresentationExchange present_proof_records_pres_ex_id_send_presentation_post(pres_ex_id)

Sends a proof presentation

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
from openapi_client.model.v10_presentation_exchange import V10PresentationExchange
from openapi_client.model.indy_pres_spec import IndyPresSpec
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier
    body = IndyPresSpec(
        requested_attributes={
            "key": IndyRequestedCredsRequestedAttr(
                cred_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
                revealed=True,
            ),
        },
        requested_predicates={
            "key": IndyRequestedCredsRequestedPred(
                cred_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
                timestamp=1640995199,
            ),
        },
        self_attested_attributes={
            "key": "self_attested_value",
        },
        trace=False,
    ) # IndyPresSpec |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Sends a proof presentation
        api_response = api_instance.present_proof_records_pres_ex_id_send_presentation_post(pres_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_send_presentation_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a proof presentation
        api_response = api_instance.present_proof_records_pres_ex_id_send_presentation_post(pres_ex_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_send_presentation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |
 **body** | [**IndyPresSpec**](IndyPresSpec.md)|  | [optional]

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_records_pres_ex_id_send_request_post**
> V10PresentationExchange present_proof_records_pres_ex_id_send_request_post(pres_ex_id)

Sends a presentation request in reference to a proposal

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
from openapi_client.model.v10_presentation_exchange import V10PresentationExchange
from openapi_client.model.admin_api_message_tracing import AdminAPIMessageTracing
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier
    body = AdminAPIMessageTracing(
        trace=True,
    ) # AdminAPIMessageTracing |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Sends a presentation request in reference to a proposal
        api_response = api_instance.present_proof_records_pres_ex_id_send_request_post(pres_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_send_request_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a presentation request in reference to a proposal
        api_response = api_instance.present_proof_records_pres_ex_id_send_request_post(pres_ex_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_send_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |
 **body** | [**AdminAPIMessageTracing**](AdminAPIMessageTracing.md)|  | [optional]

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_records_pres_ex_id_verify_presentation_post**
> V10PresentationExchange present_proof_records_pres_ex_id_verify_presentation_post(pres_ex_id)

Verify a received presentation

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
from openapi_client.model.v10_presentation_exchange import V10PresentationExchange
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    pres_ex_id = "pres_ex_id_example" # str | Presentation exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Verify a received presentation
        api_response = api_instance.present_proof_records_pres_ex_id_verify_presentation_post(pres_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_records_pres_ex_id_verify_presentation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pres_ex_id** | **str**| Presentation exchange identifier |

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_send_proposal_post**
> V10PresentationExchange present_proof_send_proposal_post()

Sends a presentation proposal

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
from openapi_client.model.v10_presentation_exchange import V10PresentationExchange
from openapi_client.model.v10_presentation_proposal_request import V10PresentationProposalRequest
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    body = V10PresentationProposalRequest(
        auto_present=True,
        comment="comment_example",
        connection_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        presentation_proposal=IndyPresPreview(
            type="did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/present-proof/1.0/presentation-preview",
            attributes=[
                IndyPresAttrSpec(
                    cred_def_id="WgWxqztrNooG92RXvxSTWv:3:CL:20:tag",
                    mime_type="image/jpeg",
                    name="favourite_drink",
                    referent="0",
                    value="martini",
                ),
            ],
            predicates=[
                IndyPresPredSpec(
                    cred_def_id="WgWxqztrNooG92RXvxSTWv:3:CL:20:tag",
                    name="high_score",
                    predicate=">=",
                    threshold=1,
                ),
            ],
        ),
        trace=False,
    ) # V10PresentationProposalRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a presentation proposal
        api_response = api_instance.present_proof_send_proposal_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_send_proposal_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10PresentationProposalRequest**](V10PresentationProposalRequest.md)|  | [optional]

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

# **present_proof_send_request_post**
> V10PresentationExchange present_proof_send_request_post()

Sends a free presentation request not bound to any proposal

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import present_proof_v1_0_api
from openapi_client.model.v10_presentation_exchange import V10PresentationExchange
from openapi_client.model.v10_presentation_send_request_request import V10PresentationSendRequestRequest
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
    api_instance = present_proof_v1_0_api.PresentProofV10Api(api_client)
    body = V10PresentationSendRequestRequest(
        comment="comment_example",
        connection_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        proof_request=IndyProofRequest(
            name="Proof request",
            non_revoked={},
            nonce="1",
            requested_attributes={
                "key": IndyProofReqAttrSpec(
                    name="favouriteDrink",
                    names=[
                        "age",
                    ],
                    non_revoked={},
                    restrictions=[
                        {
                            "key": "WgWxqztrNooG92RXvxSTWv:3:CL:20:tag",
                        },
                    ],
                ),
            },
            requested_predicates={
                "key": IndyProofReqPredSpec(
                    name="index",
                    non_revoked={},
                    p_type=">=",
                    p_value=1,
                    restrictions=[
                        {
                            "key": "WgWxqztrNooG92RXvxSTWv:3:CL:20:tag",
                        },
                    ],
                ),
            },
            version="1.0",
        ),
        trace=False,
    ) # V10PresentationSendRequestRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends a free presentation request not bound to any proposal
        api_response = api_instance.present_proof_send_request_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PresentProofV10Api->present_proof_send_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10PresentationSendRequestRequest**](V10PresentationSendRequestRequest.md)|  | [optional]

### Return type

[**V10PresentationExchange**](V10PresentationExchange.md)

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

