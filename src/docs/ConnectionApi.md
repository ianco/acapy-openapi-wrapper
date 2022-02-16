# openapi_client.ConnectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connections_conn_id_accept_invitation_post**](ConnectionApi.md#connections_conn_id_accept_invitation_post) | **POST** /connections/{conn_id}/accept-invitation | Accept a stored connection invitation
[**connections_conn_id_accept_request_post**](ConnectionApi.md#connections_conn_id_accept_request_post) | **POST** /connections/{conn_id}/accept-request | Accept a stored connection request
[**connections_conn_id_delete**](ConnectionApi.md#connections_conn_id_delete) | **DELETE** /connections/{conn_id} | Remove an existing connection record
[**connections_conn_id_endpoints_get**](ConnectionApi.md#connections_conn_id_endpoints_get) | **GET** /connections/{conn_id}/endpoints | Fetch connection remote endpoint
[**connections_conn_id_establish_inbound_ref_id_post**](ConnectionApi.md#connections_conn_id_establish_inbound_ref_id_post) | **POST** /connections/{conn_id}/establish-inbound/{ref_id} | Assign another connection as the inbound connection
[**connections_conn_id_get**](ConnectionApi.md#connections_conn_id_get) | **GET** /connections/{conn_id} | Fetch a single connection record
[**connections_conn_id_metadata_get**](ConnectionApi.md#connections_conn_id_metadata_get) | **GET** /connections/{conn_id}/metadata | Fetch connection metadata
[**connections_conn_id_metadata_post**](ConnectionApi.md#connections_conn_id_metadata_post) | **POST** /connections/{conn_id}/metadata | Set connection metadata
[**connections_create_invitation_post**](ConnectionApi.md#connections_create_invitation_post) | **POST** /connections/create-invitation | Create a new connection invitation
[**connections_create_static_post**](ConnectionApi.md#connections_create_static_post) | **POST** /connections/create-static | Create a new static connection
[**connections_get**](ConnectionApi.md#connections_get) | **GET** /connections | Query agent-to-agent connections
[**connections_receive_invitation_post**](ConnectionApi.md#connections_receive_invitation_post) | **POST** /connections/receive-invitation | Receive a new connection invitation


# **connections_conn_id_accept_invitation_post**
> ConnRecord connections_conn_id_accept_invitation_post(conn_id)

Accept a stored connection invitation

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
from openapi_client.model.conn_record import ConnRecord
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
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    my_endpoint = "1://2ZBkPowtM:.2mAWlc:fJP2zheL>AVzcDwJaHM5W71x3OA5wt6cgd/3DLuV1SPO[O[0piU4M>ZcCV8NHVTOu=9.M<9v;JgIYOjUN3M^xwdui<wL<J.3Sg>lh6mGU4?oOSM]?KyR4z2b[67Lb2O;EZW[.sGrdYN^>S8Z>.rIuc0q4W^ubSz>UKyZN]Uhr=:k626:krDb]IhF3Q0;k_1=;xhBT6t_j]uvynNKi<<D7W9QyArM?Wsyk8i.:cV]DTsGWVMl8r<aKzYn>WSlJVDQC=KkmHeibvK<zZ8tu4k89wS/vQa.x0[t18zCMZ:.2H@CgJ@_0pU?lvdC9kLstr_b_VMv>Q\.q:veBQHMXk82i1@J_ERlUFQlOC4ycWQ>?=@=;71k@m5>rI^=3Y5o=N6\\qhcqs9vGyuJECCBPm:SOcE/PqFq5flMel::<f_ax3GAOnDl1_3kXz[5aTutKLSdzgDGj0?dTOBq3K@\]RQjvWI[LW5Wt=S/yqo8QaiglWk.XniPitvYTNi^J\UYjYQF\;Tg4wjCl\jnKkRW8Z;O5YEYvCqRU4;wXZhKLp[r/kaaVVAa:\cyhy0J<Nb?5vWJ\weJan:hpO4mX7^FF2VKRi=SD3y6V9te\EXD0LJzv1[99J@a>xy/l1wmDSGP;@3UGuA=G0wBVxrv1V7DNK6\5y/FuJxmseJ<re3FEQM[^?[.wPU[B5x^zYF;723afY69LWgpl;<.iJtkbSH0_eK5d^EM_>Hi04TJ0yR^r6h\ks_PWyTSNGGGHSQ^wcxc6sRs4i@DD_wA5QPJ4L3tUji;uxx8l\qfF;CufVhUle3@JeTJwPR7_EkZ:[U.[Up4KL.gM0szYpZ2OGnkB>IQZ2ud:Oi9T]xkyGj^J=MgOnWuw]3MfBCnQDB_Rnp:dBvO1U>G0]^eZbtj2XYR?vj2>@<ONINh?baF9=3fH2xNYJ4;XTz/cWwH=OHuN9j7dDFSKnwgp[K1lR\jJGg2iP1B8Cq/vZgj73nkVCodZASPC?=FxT;nwJlQ1i.faaCxWHMK\.KtZVRD5aU7.\qKUNhA3p?SFpTNKxVxWt3uENIA^YGrK<TD=J0]RVnkw91tegY:C[idn/OeKUQ\SaFs@ezr?olRCmyNgXDZjWRa66ZZvs80jSd:aZp^c@tydWmKL@n387f\iw@jhf9?YCi9.k<etz:;TlZuFF?XP]UAau=wkqdLjAgZveuvvrnz>?HmU86fR]19mCVwX1m7oem;FNdUztTiDj/]vgIfB?bjm[MBK2fK9Q@^ZBLs1y=\^lnhy7r:KaP6Nr8>oj./x\@eYst[[[q;utllWch<OP]QLz^@p;8[P;A:62VmqyoYPwbMV8=^QcXnAie6QYL=7QjAODkaYxm^ijACd[d@ZbZsCUCR2CAe8NGpef6hv/jkTrpjrhkZZc3^iDZLFjFy7Kd?omTHV6rSJl;Kf95Sqfs^=ZI]MYjv4vs?JTVVOWll<PrKqxHD@Yd8RXMksNvuZ5UOEhpzgjjE@n3kTod]A=MIG1fQ>8SvciAtI579braxAKgVmcj4vAUjQSUlZYxYH9Eco7vL.UVnOqeeboIihEcr^i31xzYyHq=ynFesIT=2\po=zUpNUW=F[e>jSQ7/^V/K_iH?LQbQX>npfpN7D.s5]N0jQCf8bzl4ra<g;fZfyV<oihN@wAYaMLeeHYl<usTX5ei3Wkz5aGdrk9XKdsAH\Zo<Qqy?IJTS<4u7gPWInm=>;NskARjH7=3;Q_A?T;?WS\GYQXg=yI>PCDcdfzsOp>>T@;JSWKzdQ?Hp:3o=y39tpo?Szpk6fXEUxDSScjKh5RJj6s7peC;zJa82WeBA][aved6U0j7432Zz]kR@_iN.S_TwN@Ve?a7p<WLlTEOfT6Ci6YPUCQw\m=@oa/?qm1KV7gg_K7zX3BeBVZnublvB9M[7m46fFAg:l0>Ae?ADeKgQJWth1kxAxV0c[6@IgzWIQ9[BfWtF?EkNF0Z@Zu]G^kZJTKwa\Rw3bX=z;Z9/O9MG^/ZN</U<OUpnPF2abHEB.hDPtGZnF9oD?rj?how27:NtVehlwv[IfREg[\xrAgCI<Lg8d4vbq=r3sM;o;gMDOMCDjh>rNEkKLN@/PdA5q_CG=k:]m0gKPSWD9wzr4BaW\;<W[kx:A=4xxW_\btwG1t\TiB:4oM8u<TaY>o2qY9rUuB@>3Q?B9FPGJy7MCG>InI[g8QPmd" # str | My URL endpoint (optional)
    my_label = "my_label_example" # str | Label for connection (optional)

    # example passing only required values which don't have defaults set
    try:
        # Accept a stored connection invitation
        api_response = api_instance.connections_conn_id_accept_invitation_post(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_accept_invitation_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept a stored connection invitation
        api_response = api_instance.connections_conn_id_accept_invitation_post(conn_id, mediation_id=mediation_id, my_endpoint=my_endpoint, my_label=my_label)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_accept_invitation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
 **my_endpoint** | **str**| My URL endpoint | [optional]
 **my_label** | **str**| Label for connection | [optional]

### Return type

[**ConnRecord**](ConnRecord.md)

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

# **connections_conn_id_accept_request_post**
> ConnRecord connections_conn_id_accept_request_post(conn_id)

Accept a stored connection request

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
from openapi_client.model.conn_record import ConnRecord
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
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    my_endpoint = "1://2ZBkPowtM:.2mAWlc:fJP2zheL>AVzcDwJaHM5W71x3OA5wt6cgd/3DLuV1SPO[O[0piU4M>ZcCV8NHVTOu=9.M<9v;JgIYOjUN3M^xwdui<wL<J.3Sg>lh6mGU4?oOSM]?KyR4z2b[67Lb2O;EZW[.sGrdYN^>S8Z>.rIuc0q4W^ubSz>UKyZN]Uhr=:k626:krDb]IhF3Q0;k_1=;xhBT6t_j]uvynNKi<<D7W9QyArM?Wsyk8i.:cV]DTsGWVMl8r<aKzYn>WSlJVDQC=KkmHeibvK<zZ8tu4k89wS/vQa.x0[t18zCMZ:.2H@CgJ@_0pU?lvdC9kLstr_b_VMv>Q\.q:veBQHMXk82i1@J_ERlUFQlOC4ycWQ>?=@=;71k@m5>rI^=3Y5o=N6\\qhcqs9vGyuJECCBPm:SOcE/PqFq5flMel::<f_ax3GAOnDl1_3kXz[5aTutKLSdzgDGj0?dTOBq3K@\]RQjvWI[LW5Wt=S/yqo8QaiglWk.XniPitvYTNi^J\UYjYQF\;Tg4wjCl\jnKkRW8Z;O5YEYvCqRU4;wXZhKLp[r/kaaVVAa:\cyhy0J<Nb?5vWJ\weJan:hpO4mX7^FF2VKRi=SD3y6V9te\EXD0LJzv1[99J@a>xy/l1wmDSGP;@3UGuA=G0wBVxrv1V7DNK6\5y/FuJxmseJ<re3FEQM[^?[.wPU[B5x^zYF;723afY69LWgpl;<.iJtkbSH0_eK5d^EM_>Hi04TJ0yR^r6h\ks_PWyTSNGGGHSQ^wcxc6sRs4i@DD_wA5QPJ4L3tUji;uxx8l\qfF;CufVhUle3@JeTJwPR7_EkZ:[U.[Up4KL.gM0szYpZ2OGnkB>IQZ2ud:Oi9T]xkyGj^J=MgOnWuw]3MfBCnQDB_Rnp:dBvO1U>G0]^eZbtj2XYR?vj2>@<ONINh?baF9=3fH2xNYJ4;XTz/cWwH=OHuN9j7dDFSKnwgp[K1lR\jJGg2iP1B8Cq/vZgj73nkVCodZASPC?=FxT;nwJlQ1i.faaCxWHMK\.KtZVRD5aU7.\qKUNhA3p?SFpTNKxVxWt3uENIA^YGrK<TD=J0]RVnkw91tegY:C[idn/OeKUQ\SaFs@ezr?olRCmyNgXDZjWRa66ZZvs80jSd:aZp^c@tydWmKL@n387f\iw@jhf9?YCi9.k<etz:;TlZuFF?XP]UAau=wkqdLjAgZveuvvrnz>?HmU86fR]19mCVwX1m7oem;FNdUztTiDj/]vgIfB?bjm[MBK2fK9Q@^ZBLs1y=\^lnhy7r:KaP6Nr8>oj./x\@eYst[[[q;utllWch<OP]QLz^@p;8[P;A:62VmqyoYPwbMV8=^QcXnAie6QYL=7QjAODkaYxm^ijACd[d@ZbZsCUCR2CAe8NGpef6hv/jkTrpjrhkZZc3^iDZLFjFy7Kd?omTHV6rSJl;Kf95Sqfs^=ZI]MYjv4vs?JTVVOWll<PrKqxHD@Yd8RXMksNvuZ5UOEhpzgjjE@n3kTod]A=MIG1fQ>8SvciAtI579braxAKgVmcj4vAUjQSUlZYxYH9Eco7vL.UVnOqeeboIihEcr^i31xzYyHq=ynFesIT=2\po=zUpNUW=F[e>jSQ7/^V/K_iH?LQbQX>npfpN7D.s5]N0jQCf8bzl4ra<g;fZfyV<oihN@wAYaMLeeHYl<usTX5ei3Wkz5aGdrk9XKdsAH\Zo<Qqy?IJTS<4u7gPWInm=>;NskARjH7=3;Q_A?T;?WS\GYQXg=yI>PCDcdfzsOp>>T@;JSWKzdQ?Hp:3o=y39tpo?Szpk6fXEUxDSScjKh5RJj6s7peC;zJa82WeBA][aved6U0j7432Zz]kR@_iN.S_TwN@Ve?a7p<WLlTEOfT6Ci6YPUCQw\m=@oa/?qm1KV7gg_K7zX3BeBVZnublvB9M[7m46fFAg:l0>Ae?ADeKgQJWth1kxAxV0c[6@IgzWIQ9[BfWtF?EkNF0Z@Zu]G^kZJTKwa\Rw3bX=z;Z9/O9MG^/ZN</U<OUpnPF2abHEB.hDPtGZnF9oD?rj?how27:NtVehlwv[IfREg[\xrAgCI<Lg8d4vbq=r3sM;o;gMDOMCDjh>rNEkKLN@/PdA5q_CG=k:]m0gKPSWD9wzr4BaW\;<W[kx:A=4xxW_\btwG1t\TiB:4oM8u<TaY>o2qY9rUuB@>3Q?B9FPGJy7MCG>InI[g8QPmd" # str | My URL endpoint (optional)

    # example passing only required values which don't have defaults set
    try:
        # Accept a stored connection request
        api_response = api_instance.connections_conn_id_accept_request_post(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_accept_request_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept a stored connection request
        api_response = api_instance.connections_conn_id_accept_request_post(conn_id, my_endpoint=my_endpoint)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_accept_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **my_endpoint** | **str**| My URL endpoint | [optional]

### Return type

[**ConnRecord**](ConnRecord.md)

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

# **connections_conn_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type connections_conn_id_delete(conn_id)

Remove an existing connection record

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
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
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Remove an existing connection record
        api_response = api_instance.connections_conn_id_delete(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |

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

# **connections_conn_id_endpoints_get**
> EndpointsResult connections_conn_id_endpoints_get(conn_id)

Fetch connection remote endpoint

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
from openapi_client.model.endpoints_result import EndpointsResult
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
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch connection remote endpoint
        api_response = api_instance.connections_conn_id_endpoints_get(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_endpoints_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |

### Return type

[**EndpointsResult**](EndpointsResult.md)

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

# **connections_conn_id_establish_inbound_ref_id_post**
> bool, date, datetime, dict, float, int, list, str, none_type connections_conn_id_establish_inbound_ref_id_post(conn_id, ref_id)

Assign another connection as the inbound connection

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
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
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    ref_id = "ref_id_example" # str | Inbound connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Assign another connection as the inbound connection
        api_response = api_instance.connections_conn_id_establish_inbound_ref_id_post(conn_id, ref_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_establish_inbound_ref_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **ref_id** | **str**| Inbound connection identifier |

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

# **connections_conn_id_get**
> ConnRecord connections_conn_id_get(conn_id)

Fetch a single connection record

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
from openapi_client.model.conn_record import ConnRecord
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
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier

    # example passing only required values which don't have defaults set
    try:
        # Fetch a single connection record
        api_response = api_instance.connections_conn_id_get(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |

### Return type

[**ConnRecord**](ConnRecord.md)

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

# **connections_conn_id_metadata_get**
> ConnectionMetadata connections_conn_id_metadata_get(conn_id)

Fetch connection metadata

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
from openapi_client.model.connection_metadata import ConnectionMetadata
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
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    key = "key_example" # str | Key to retrieve. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch connection metadata
        api_response = api_instance.connections_conn_id_metadata_get(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_metadata_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch connection metadata
        api_response = api_instance.connections_conn_id_metadata_get(conn_id, key=key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_metadata_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **key** | **str**| Key to retrieve. | [optional]

### Return type

[**ConnectionMetadata**](ConnectionMetadata.md)

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

# **connections_conn_id_metadata_post**
> ConnectionMetadata connections_conn_id_metadata_post(conn_id)

Set connection metadata

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
from openapi_client.model.connection_metadata_set_request import ConnectionMetadataSetRequest
from openapi_client.model.connection_metadata import ConnectionMetadata
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
    api_instance = connection_api.ConnectionApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    body = ConnectionMetadataSetRequest(
        metadata={},
    ) # ConnectionMetadataSetRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set connection metadata
        api_response = api_instance.connections_conn_id_metadata_post(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_metadata_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set connection metadata
        api_response = api_instance.connections_conn_id_metadata_post(conn_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_conn_id_metadata_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **body** | [**ConnectionMetadataSetRequest**](ConnectionMetadataSetRequest.md)|  | [optional]

### Return type

[**ConnectionMetadata**](ConnectionMetadata.md)

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

# **connections_create_invitation_post**
> InvitationResult connections_create_invitation_post()

Create a new connection invitation

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
from openapi_client.model.create_invitation_request import CreateInvitationRequest
from openapi_client.model.invitation_result import InvitationResult
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
    api_instance = connection_api.ConnectionApi(api_client)
    alias = "alias_example" # str | Alias (optional)
    auto_accept = True # bool | Auto-accept connection (defaults to configuration) (optional)
    multi_use = True # bool | Create invitation for multiple use (default false) (optional)
    public = True # bool | Create invitation from public DID (default false) (optional)
    body = CreateInvitationRequest(
        mediation_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        metadata={},
        my_label="Bob",
        recipient_keys=[
            "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV",
        ],
        routing_keys=[
            "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV",
        ],
        service_endpoint="http://192.168.56.102:8020",
    ) # CreateInvitationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new connection invitation
        api_response = api_instance.connections_create_invitation_post(alias=alias, auto_accept=auto_accept, multi_use=multi_use, public=public, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_create_invitation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias | [optional]
 **auto_accept** | **bool**| Auto-accept connection (defaults to configuration) | [optional]
 **multi_use** | **bool**| Create invitation for multiple use (default false) | [optional]
 **public** | **bool**| Create invitation from public DID (default false) | [optional]
 **body** | [**CreateInvitationRequest**](CreateInvitationRequest.md)|  | [optional]

### Return type

[**InvitationResult**](InvitationResult.md)

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

# **connections_create_static_post**
> ConnectionStaticResult connections_create_static_post()

Create a new static connection

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
from openapi_client.model.connection_static_result import ConnectionStaticResult
from openapi_client.model.connection_static_request import ConnectionStaticRequest
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
    api_instance = connection_api.ConnectionApi(api_client)
    body = ConnectionStaticRequest(
        alias="alias_example",
        my_did="WgWxqztrNooG92RXvxSTWv",
        my_seed="my_seed_example",
        their_did="WgWxqztrNooG92RXvxSTWv",
        their_endpoint="https://myhost:8021",
        their_label="their_label_example",
        their_seed="their_seed_example",
        their_verkey="their_verkey_example",
    ) # ConnectionStaticRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new static connection
        api_response = api_instance.connections_create_static_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_create_static_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionStaticRequest**](ConnectionStaticRequest.md)|  | [optional]

### Return type

[**ConnectionStaticResult**](ConnectionStaticResult.md)

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

# **connections_get**
> ConnectionList connections_get()

Query agent-to-agent connections

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
from openapi_client.model.connection_list import ConnectionList
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
    api_instance = connection_api.ConnectionApi(api_client)
    alias = "alias_example" # str | Alias (optional)
    connection_protocol = "connections/1.0" # str | Connection protocol used (optional)
    invitation_key = "FZPn3BZqhoxS1o7RzixZRE9TRJrjhKGPim39DqZKtY2C" # str | invitation key (optional)
    my_did = "did:sov:ZPn3BZqhoxS1o7RzixZRE9" # str | My DID (optional)
    state = "abandoned" # str | Connection state (optional)
    their_did = "did:sov:ZPn3BZqhoxS1o7RzixZRE9" # str | Their DID (optional)
    their_role = "invitee" # str | Their role in the connection protocol (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query agent-to-agent connections
        api_response = api_instance.connections_get(alias=alias, connection_protocol=connection_protocol, invitation_key=invitation_key, my_did=my_did, state=state, their_did=their_did, their_role=their_role)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias | [optional]
 **connection_protocol** | **str**| Connection protocol used | [optional]
 **invitation_key** | **str**| invitation key | [optional]
 **my_did** | **str**| My DID | [optional]
 **state** | **str**| Connection state | [optional]
 **their_did** | **str**| Their DID | [optional]
 **their_role** | **str**| Their role in the connection protocol | [optional]

### Return type

[**ConnectionList**](ConnectionList.md)

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

# **connections_receive_invitation_post**
> ConnRecord connections_receive_invitation_post()

Receive a new connection invitation

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import connection_api
from openapi_client.model.conn_record import ConnRecord
from openapi_client.model.receive_invitation_request import ReceiveInvitationRequest
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
    api_instance = connection_api.ConnectionApi(api_client)
    alias = "alias_example" # str | Alias (optional)
    auto_accept = True # bool | Auto-accept connection (defaults to configuration) (optional)
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    body = ReceiveInvitationRequest(
        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        did="WgWxqztrNooG92RXvxSTWv",
        image_url="http://192.168.56.101/img/logo.jpg",
        label="Bob",
        recipient_keys=[
            "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV",
        ],
        routing_keys=[
            "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV",
        ],
        service_endpoint="http://192.168.56.101:8020",
    ) # ReceiveInvitationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Receive a new connection invitation
        api_response = api_instance.connections_receive_invitation_post(alias=alias, auto_accept=auto_accept, mediation_id=mediation_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConnectionApi->connections_receive_invitation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias | [optional]
 **auto_accept** | **bool**| Auto-accept connection (defaults to configuration) | [optional]
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
 **body** | [**ReceiveInvitationRequest**](ReceiveInvitationRequest.md)|  | [optional]

### Return type

[**ConnRecord**](ConnRecord.md)

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

