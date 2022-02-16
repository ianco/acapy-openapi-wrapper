# openapi_client.IssueCredentialV20Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_credential20_create_offer_post**](IssueCredentialV20Api.md#issue_credential20_create_offer_post) | **POST** /issue-credential-2.0/create-offer | Create a credential offer, independent of any proposal or connection
[**issue_credential20_create_post**](IssueCredentialV20Api.md#issue_credential20_create_post) | **POST** /issue-credential-2.0/create | Create credential from attribute values
[**issue_credential20_records_cred_ex_id_delete**](IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_delete) | **DELETE** /issue-credential-2.0/records/{cred_ex_id} | Remove an existing credential exchange record
[**issue_credential20_records_cred_ex_id_get**](IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_get) | **GET** /issue-credential-2.0/records/{cred_ex_id} | Fetch a single credential exchange record
[**issue_credential20_records_cred_ex_id_issue_post**](IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_issue_post) | **POST** /issue-credential-2.0/records/{cred_ex_id}/issue | Send holder a credential
[**issue_credential20_records_cred_ex_id_problem_report_post**](IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_problem_report_post) | **POST** /issue-credential-2.0/records/{cred_ex_id}/problem-report | Send a problem report for credential exchange
[**issue_credential20_records_cred_ex_id_send_offer_post**](IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_send_offer_post) | **POST** /issue-credential-2.0/records/{cred_ex_id}/send-offer | Send holder a credential offer in reference to a proposal with preview
[**issue_credential20_records_cred_ex_id_send_request_post**](IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_send_request_post) | **POST** /issue-credential-2.0/records/{cred_ex_id}/send-request | Send issuer a credential request
[**issue_credential20_records_cred_ex_id_store_post**](IssueCredentialV20Api.md#issue_credential20_records_cred_ex_id_store_post) | **POST** /issue-credential-2.0/records/{cred_ex_id}/store | Store a received credential
[**issue_credential20_records_get**](IssueCredentialV20Api.md#issue_credential20_records_get) | **GET** /issue-credential-2.0/records | Fetch all credential exchange records
[**issue_credential20_send_offer_post**](IssueCredentialV20Api.md#issue_credential20_send_offer_post) | **POST** /issue-credential-2.0/send-offer | Send holder a credential offer, independent of any proposal
[**issue_credential20_send_post**](IssueCredentialV20Api.md#issue_credential20_send_post) | **POST** /issue-credential-2.0/send | Send holder a credential, automating entire flow
[**issue_credential20_send_proposal_post**](IssueCredentialV20Api.md#issue_credential20_send_proposal_post) | **POST** /issue-credential-2.0/send-proposal | Send issuer a credential proposal
[**issue_credential20_send_request_post**](IssueCredentialV20Api.md#issue_credential20_send_request_post) | **POST** /issue-credential-2.0/send-request | Send issuer a credential request not bound to an existing thread. Indy credentials cannot start at a request


# **issue_credential20_create_offer_post**
> V20CredExRecord issue_credential20_create_offer_post()

Create a credential offer, independent of any proposal or connection

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_offer_conn_free_request import V20CredOfferConnFreeRequest
from openapi_client.model.v20_cred_ex_record import V20CredExRecord
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    body = V20CredOfferConnFreeRequest(
        auto_issue=True,
        auto_remove=True,
        comment="comment_example",
        credential_preview=V20CredPreview(
            type="issue-credential/2.0/credential-preview",
            attributes=[
                V20CredAttrSpec(
                    mime_type="image/jpeg",
                    name="favourite_drink",
                    value="martini",
                ),
            ],
        ),
        filter={},
        trace=True,
    ) # V20CredOfferConnFreeRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a credential offer, independent of any proposal or connection
        api_response = api_instance.issue_credential20_create_offer_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_create_offer_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V20CredOfferConnFreeRequest**](V20CredOfferConnFreeRequest.md)|  | [optional]

### Return type

[**V20CredExRecord**](V20CredExRecord.md)

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

# **issue_credential20_create_post**
> V20CredExRecord issue_credential20_create_post()

Create credential from attribute values

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_issue_cred_schema_core import V20IssueCredSchemaCore
from openapi_client.model.v20_cred_ex_record import V20CredExRecord
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    body = V20IssueCredSchemaCore(
        auto_remove=True,
        comment="comment_example",
        credential_preview=V20CredPreview(
            type="issue-credential/2.0/credential-preview",
            attributes=[
                V20CredAttrSpec(
                    mime_type="image/jpeg",
                    name="favourite_drink",
                    value="martini",
                ),
            ],
        ),
        filter={},
        trace=True,
    ) # V20IssueCredSchemaCore |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create credential from attribute values
        api_response = api_instance.issue_credential20_create_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_create_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V20IssueCredSchemaCore**](V20IssueCredSchemaCore.md)|  | [optional]

### Return type

[**V20CredExRecord**](V20CredExRecord.md)

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

# **issue_credential20_records_cred_ex_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type issue_credential20_records_cred_ex_id_delete(cred_ex_id)

Remove an existing credential exchange record

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove an existing credential exchange record
        api_response = api_instance.issue_credential20_records_cred_ex_id_delete(cred_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |

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

# **issue_credential20_records_cred_ex_id_get**
> V20CredExRecordDetail issue_credential20_records_cred_ex_id_get(cred_ex_id)

Fetch a single credential exchange record

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_ex_record_detail import V20CredExRecordDetail
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch a single credential exchange record
        api_response = api_instance.issue_credential20_records_cred_ex_id_get(cred_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |

### Return type

[**V20CredExRecordDetail**](V20CredExRecordDetail.md)

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

# **issue_credential20_records_cred_ex_id_issue_post**
> V20CredExRecordDetail issue_credential20_records_cred_ex_id_issue_post(cred_ex_id)

Send holder a credential

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_ex_record_detail import V20CredExRecordDetail
from openapi_client.model.v20_cred_issue_request import V20CredIssueRequest
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier
    body = V20CredIssueRequest(
        comment="comment_example",
    ) # V20CredIssueRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send holder a credential
        api_response = api_instance.issue_credential20_records_cred_ex_id_issue_post(cred_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_issue_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send holder a credential
        api_response = api_instance.issue_credential20_records_cred_ex_id_issue_post(cred_ex_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_issue_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |
 **body** | [**V20CredIssueRequest**](V20CredIssueRequest.md)|  | [optional]

### Return type

[**V20CredExRecordDetail**](V20CredExRecordDetail.md)

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

# **issue_credential20_records_cred_ex_id_problem_report_post**
> bool, date, datetime, dict, float, int, list, str, none_type issue_credential20_records_cred_ex_id_problem_report_post(cred_ex_id)

Send a problem report for credential exchange

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_issue_problem_report_request import V20CredIssueProblemReportRequest
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier
    body = V20CredIssueProblemReportRequest(
        description="description_example",
    ) # V20CredIssueProblemReportRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a problem report for credential exchange
        api_response = api_instance.issue_credential20_records_cred_ex_id_problem_report_post(cred_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_problem_report_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a problem report for credential exchange
        api_response = api_instance.issue_credential20_records_cred_ex_id_problem_report_post(cred_ex_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_problem_report_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |
 **body** | [**V20CredIssueProblemReportRequest**](V20CredIssueProblemReportRequest.md)|  | [optional]

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

# **issue_credential20_records_cred_ex_id_send_offer_post**
> V20CredExRecord issue_credential20_records_cred_ex_id_send_offer_post(cred_ex_id)

Send holder a credential offer in reference to a proposal with preview

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_bound_offer_request import V20CredBoundOfferRequest
from openapi_client.model.v20_cred_ex_record import V20CredExRecord
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier
    body = V20CredBoundOfferRequest(
        counter_preview={},
        filter={},
    ) # V20CredBoundOfferRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send holder a credential offer in reference to a proposal with preview
        api_response = api_instance.issue_credential20_records_cred_ex_id_send_offer_post(cred_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_send_offer_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send holder a credential offer in reference to a proposal with preview
        api_response = api_instance.issue_credential20_records_cred_ex_id_send_offer_post(cred_ex_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_send_offer_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |
 **body** | [**V20CredBoundOfferRequest**](V20CredBoundOfferRequest.md)|  | [optional]

### Return type

[**V20CredExRecord**](V20CredExRecord.md)

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

# **issue_credential20_records_cred_ex_id_send_request_post**
> V20CredExRecord issue_credential20_records_cred_ex_id_send_request_post(cred_ex_id)

Send issuer a credential request

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_request_request import V20CredRequestRequest
from openapi_client.model.v20_cred_ex_record import V20CredExRecord
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier
    body = V20CredRequestRequest(
        holder_did="did:key:ahsdkjahsdkjhaskjdhakjshdkajhsdkjahs",
    ) # V20CredRequestRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send issuer a credential request
        api_response = api_instance.issue_credential20_records_cred_ex_id_send_request_post(cred_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_send_request_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send issuer a credential request
        api_response = api_instance.issue_credential20_records_cred_ex_id_send_request_post(cred_ex_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_send_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |
 **body** | [**V20CredRequestRequest**](V20CredRequestRequest.md)|  | [optional]

### Return type

[**V20CredExRecord**](V20CredExRecord.md)

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

# **issue_credential20_records_cred_ex_id_store_post**
> V20CredExRecordDetail issue_credential20_records_cred_ex_id_store_post(cred_ex_id)

Store a received credential

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_ex_record_detail import V20CredExRecordDetail
from openapi_client.model.v20_cred_store_request import V20CredStoreRequest
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    cred_ex_id = "cred_ex_id_example" # str | Credential exchange identifier
    body = V20CredStoreRequest(
        credential_id="credential_id_example",
    ) # V20CredStoreRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Store a received credential
        api_response = api_instance.issue_credential20_records_cred_ex_id_store_post(cred_ex_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_store_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Store a received credential
        api_response = api_instance.issue_credential20_records_cred_ex_id_store_post(cred_ex_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_cred_ex_id_store_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_ex_id** | **str**| Credential exchange identifier |
 **body** | [**V20CredStoreRequest**](V20CredStoreRequest.md)|  | [optional]

### Return type

[**V20CredExRecordDetail**](V20CredExRecordDetail.md)

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

# **issue_credential20_records_get**
> V20CredExRecordListResult issue_credential20_records_get()

Fetch all credential exchange records

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_ex_record_list_result import V20CredExRecordListResult
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    connection_id = "connection_id_example" # str | Connection identifier (optional)
    role = "issuer" # str | Role assigned in credential exchange (optional)
    state = "proposal-sent" # str | Credential exchange state (optional)
    thread_id = "thread_id_example" # str | Thread identifier (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all credential exchange records
        api_response = api_instance.issue_credential20_records_get(connection_id=connection_id, role=role, state=state, thread_id=thread_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_records_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Connection identifier | [optional]
 **role** | **str**| Role assigned in credential exchange | [optional]
 **state** | **str**| Credential exchange state | [optional]
 **thread_id** | **str**| Thread identifier | [optional]

### Return type

[**V20CredExRecordListResult**](V20CredExRecordListResult.md)

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

# **issue_credential20_send_offer_post**
> V20CredExRecord issue_credential20_send_offer_post()

Send holder a credential offer, independent of any proposal

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_offer_request import V20CredOfferRequest
from openapi_client.model.v20_cred_ex_record import V20CredExRecord
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    body = V20CredOfferRequest(
        auto_issue=True,
        auto_remove=True,
        comment="comment_example",
        connection_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        credential_preview=V20CredPreview(
            type="issue-credential/2.0/credential-preview",
            attributes=[
                V20CredAttrSpec(
                    mime_type="image/jpeg",
                    name="favourite_drink",
                    value="martini",
                ),
            ],
        ),
        filter={},
        trace=True,
    ) # V20CredOfferRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send holder a credential offer, independent of any proposal
        api_response = api_instance.issue_credential20_send_offer_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_send_offer_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V20CredOfferRequest**](V20CredOfferRequest.md)|  | [optional]

### Return type

[**V20CredExRecord**](V20CredExRecord.md)

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

# **issue_credential20_send_post**
> V20CredExRecord issue_credential20_send_post()

Send holder a credential, automating entire flow

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_ex_free import V20CredExFree
from openapi_client.model.v20_cred_ex_record import V20CredExRecord
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    body = V20CredExFree(
        auto_remove=True,
        comment="comment_example",
        connection_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        credential_preview=V20CredPreview(
            type="issue-credential/2.0/credential-preview",
            attributes=[
                V20CredAttrSpec(
                    mime_type="image/jpeg",
                    name="favourite_drink",
                    value="martini",
                ),
            ],
        ),
        filter={},
        trace=True,
    ) # V20CredExFree |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send holder a credential, automating entire flow
        api_response = api_instance.issue_credential20_send_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_send_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V20CredExFree**](V20CredExFree.md)|  | [optional]

### Return type

[**V20CredExRecord**](V20CredExRecord.md)

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

# **issue_credential20_send_proposal_post**
> V20CredExRecord issue_credential20_send_proposal_post()

Send issuer a credential proposal

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_ex_free import V20CredExFree
from openapi_client.model.v20_cred_ex_record import V20CredExRecord
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    body = V20CredExFree(
        auto_remove=True,
        comment="comment_example",
        connection_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        credential_preview=V20CredPreview(
            type="issue-credential/2.0/credential-preview",
            attributes=[
                V20CredAttrSpec(
                    mime_type="image/jpeg",
                    name="favourite_drink",
                    value="martini",
                ),
            ],
        ),
        filter={},
        trace=True,
    ) # V20CredExFree |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send issuer a credential proposal
        api_response = api_instance.issue_credential20_send_proposal_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_send_proposal_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V20CredExFree**](V20CredExFree.md)|  | [optional]

### Return type

[**V20CredExRecord**](V20CredExRecord.md)

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

# **issue_credential20_send_request_post**
> V20CredExRecord issue_credential20_send_request_post()

Send issuer a credential request not bound to an existing thread. Indy credentials cannot start at a request

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import issue_credential_v2_0_api
from openapi_client.model.v20_cred_request_free import V20CredRequestFree
from openapi_client.model.v20_cred_ex_record import V20CredExRecord
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
    api_instance = issue_credential_v2_0_api.IssueCredentialV20Api(api_client)
    body = V20CredRequestFree(
        auto_remove=True,
        comment="comment_example",
        connection_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        filter={},
        holder_did="did:key:ahsdkjahsdkjhaskjdhakjshdkajhsdkjahs",
        trace=False,
    ) # V20CredRequestFree |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send issuer a credential request not bound to an existing thread. Indy credentials cannot start at a request
        api_response = api_instance.issue_credential20_send_request_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IssueCredentialV20Api->issue_credential20_send_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V20CredRequestFree**](V20CredRequestFree.md)|  | [optional]

### Return type

[**V20CredExRecord**](V20CredExRecord.md)

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

