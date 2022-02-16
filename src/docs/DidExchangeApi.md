# openapi_client.DidExchangeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**didexchange_conn_id_accept_invitation_post**](DidExchangeApi.md#didexchange_conn_id_accept_invitation_post) | **POST** /didexchange/{conn_id}/accept-invitation | Accept a stored connection invitation
[**didexchange_conn_id_accept_request_post**](DidExchangeApi.md#didexchange_conn_id_accept_request_post) | **POST** /didexchange/{conn_id}/accept-request | Accept a stored connection request
[**didexchange_create_request_post**](DidExchangeApi.md#didexchange_create_request_post) | **POST** /didexchange/create-request | Create and send a request against public DID&#39;s implicit invitation
[**didexchange_receive_request_post**](DidExchangeApi.md#didexchange_receive_request_post) | **POST** /didexchange/receive-request | Receive request against public DID&#39;s implicit invitation


# **didexchange_conn_id_accept_invitation_post**
> ConnRecord didexchange_conn_id_accept_invitation_post(conn_id)

Accept a stored connection invitation

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import did_exchange_api
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
    api_instance = did_exchange_api.DidExchangeApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    my_endpoint = "1://2ZBkPowtM:.2mAWlc:fJP2zheL>AVzcDwJaHM5W71x3OA5wt6cgd/3DLuV1SPO[O[0piU4M>ZcCV8NHVTOu=9.M<9v;JgIYOjUN3M^xwdui<wL<J.3Sg>lh6mGU4?oOSM]?KyR4z2b[67Lb2O;EZW[.sGrdYN^>S8Z>.rIuc0q4W^ubSz>UKyZN]Uhr=:k626:krDb]IhF3Q0;k_1=;xhBT6t_j]uvynNKi<<D7W9QyArM?Wsyk8i.:cV]DTsGWVMl8r<aKzYn>WSlJVDQC=KkmHeibvK<zZ8tu4k89wS/vQa.x0[t18zCMZ:.2H@CgJ@_0pU?lvdC9kLstr_b_VMv>Q\.q:veBQHMXk82i1@J_ERlUFQlOC4ycWQ>?=@=;71k@m5>rI^=3Y5o=N6\\qhcqs9vGyuJECCBPm:SOcE/PqFq5flMel::<f_ax3GAOnDl1_3kXz[5aTutKLSdzgDGj0?dTOBq3K@\]RQjvWI[LW5Wt=S/yqo8QaiglWk.XniPitvYTNi^J\UYjYQF\;Tg4wjCl\jnKkRW8Z;O5YEYvCqRU4;wXZhKLp[r/kaaVVAa:\cyhy0J<Nb?5vWJ\weJan:hpO4mX7^FF2VKRi=SD3y6V9te\EXD0LJzv1[99J@a>xy/l1wmDSGP;@3UGuA=G0wBVxrv1V7DNK6\5y/FuJxmseJ<re3FEQM[^?[.wPU[B5x^zYF;723afY69LWgpl;<.iJtkbSH0_eK5d^EM_>Hi04TJ0yR^r6h\ks_PWyTSNGGGHSQ^wcxc6sRs4i@DD_wA5QPJ4L3tUji;uxx8l\qfF;CufVhUle3@JeTJwPR7_EkZ:[U.[Up4KL.gM0szYpZ2OGnkB>IQZ2ud:Oi9T]xkyGj^J=MgOnWuw]3MfBCnQDB_Rnp:dBvO1U>G0]^eZbtj2XYR?vj2>@<ONINh?baF9=3fH2xNYJ4;XTz/cWwH=OHuN9j7dDFSKnwgp[K1lR\jJGg2iP1B8Cq/vZgj73nkVCodZASPC?=FxT;nwJlQ1i.faaCxWHMK\.KtZVRD5aU7.\qKUNhA3p?SFpTNKxVxWt3uENIA^YGrK<TD=J0]RVnkw91tegY:C[idn/OeKUQ\SaFs@ezr?olRCmyNgXDZjWRa66ZZvs80jSd:aZp^c@tydWmKL@n387f\iw@jhf9?YCi9.k<etz:;TlZuFF?XP]UAau=wkqdLjAgZveuvvrnz>?HmU86fR]19mCVwX1m7oem;FNdUztTiDj/]vgIfB?bjm[MBK2fK9Q@^ZBLs1y=\^lnhy7r:KaP6Nr8>oj./x\@eYst[[[q;utllWch<OP]QLz^@p;8[P;A:62VmqyoYPwbMV8=^QcXnAie6QYL=7QjAODkaYxm^ijACd[d@ZbZsCUCR2CAe8NGpef6hv/jkTrpjrhkZZc3^iDZLFjFy7Kd?omTHV6rSJl;Kf95Sqfs^=ZI]MYjv4vs?JTVVOWll<PrKqxHD@Yd8RXMksNvuZ5UOEhpzgjjE@n3kTod]A=MIG1fQ>8SvciAtI579braxAKgVmcj4vAUjQSUlZYxYH9Eco7vL.UVnOqeeboIihEcr^i31xzYyHq=ynFesIT=2\po=zUpNUW=F[e>jSQ7/^V/K_iH?LQbQX>npfpN7D.s5]N0jQCf8bzl4ra<g;fZfyV<oihN@wAYaMLeeHYl<usTX5ei3Wkz5aGdrk9XKdsAH\Zo<Qqy?IJTS<4u7gPWInm=>;NskARjH7=3;Q_A?T;?WS\GYQXg=yI>PCDcdfzsOp>>T@;JSWKzdQ?Hp:3o=y39tpo?Szpk6fXEUxDSScjKh5RJj6s7peC;zJa82WeBA][aved6U0j7432Zz]kR@_iN.S_TwN@Ve?a7p<WLlTEOfT6Ci6YPUCQw\m=@oa/?qm1KV7gg_K7zX3BeBVZnublvB9M[7m46fFAg:l0>Ae?ADeKgQJWth1kxAxV0c[6@IgzWIQ9[BfWtF?EkNF0Z@Zu]G^kZJTKwa\Rw3bX=z;Z9/O9MG^/ZN</U<OUpnPF2abHEB.hDPtGZnF9oD?rj?how27:NtVehlwv[IfREg[\xrAgCI<Lg8d4vbq=r3sM;o;gMDOMCDjh>rNEkKLN@/PdA5q_CG=k:]m0gKPSWD9wzr4BaW\;<W[kx:A=4xxW_\btwG1t\TiB:4oM8u<TaY>o2qY9rUuB@>3Q?B9FPGJy7MCG>InI[g8QPmd" # str | My URL endpoint (optional)
    my_label = "my_label_example" # str | Label for connection request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Accept a stored connection invitation
        api_response = api_instance.didexchange_conn_id_accept_invitation_post(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_conn_id_accept_invitation_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept a stored connection invitation
        api_response = api_instance.didexchange_conn_id_accept_invitation_post(conn_id, my_endpoint=my_endpoint, my_label=my_label)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_conn_id_accept_invitation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **my_endpoint** | **str**| My URL endpoint | [optional]
 **my_label** | **str**| Label for connection request | [optional]

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

# **didexchange_conn_id_accept_request_post**
> ConnRecord didexchange_conn_id_accept_request_post(conn_id)

Accept a stored connection request

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import did_exchange_api
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
    api_instance = did_exchange_api.DidExchangeApi(api_client)
    conn_id = "conn_id_example" # str | Connection identifier
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    my_endpoint = "1://2ZBkPowtM:.2mAWlc:fJP2zheL>AVzcDwJaHM5W71x3OA5wt6cgd/3DLuV1SPO[O[0piU4M>ZcCV8NHVTOu=9.M<9v;JgIYOjUN3M^xwdui<wL<J.3Sg>lh6mGU4?oOSM]?KyR4z2b[67Lb2O;EZW[.sGrdYN^>S8Z>.rIuc0q4W^ubSz>UKyZN]Uhr=:k626:krDb]IhF3Q0;k_1=;xhBT6t_j]uvynNKi<<D7W9QyArM?Wsyk8i.:cV]DTsGWVMl8r<aKzYn>WSlJVDQC=KkmHeibvK<zZ8tu4k89wS/vQa.x0[t18zCMZ:.2H@CgJ@_0pU?lvdC9kLstr_b_VMv>Q\.q:veBQHMXk82i1@J_ERlUFQlOC4ycWQ>?=@=;71k@m5>rI^=3Y5o=N6\\qhcqs9vGyuJECCBPm:SOcE/PqFq5flMel::<f_ax3GAOnDl1_3kXz[5aTutKLSdzgDGj0?dTOBq3K@\]RQjvWI[LW5Wt=S/yqo8QaiglWk.XniPitvYTNi^J\UYjYQF\;Tg4wjCl\jnKkRW8Z;O5YEYvCqRU4;wXZhKLp[r/kaaVVAa:\cyhy0J<Nb?5vWJ\weJan:hpO4mX7^FF2VKRi=SD3y6V9te\EXD0LJzv1[99J@a>xy/l1wmDSGP;@3UGuA=G0wBVxrv1V7DNK6\5y/FuJxmseJ<re3FEQM[^?[.wPU[B5x^zYF;723afY69LWgpl;<.iJtkbSH0_eK5d^EM_>Hi04TJ0yR^r6h\ks_PWyTSNGGGHSQ^wcxc6sRs4i@DD_wA5QPJ4L3tUji;uxx8l\qfF;CufVhUle3@JeTJwPR7_EkZ:[U.[Up4KL.gM0szYpZ2OGnkB>IQZ2ud:Oi9T]xkyGj^J=MgOnWuw]3MfBCnQDB_Rnp:dBvO1U>G0]^eZbtj2XYR?vj2>@<ONINh?baF9=3fH2xNYJ4;XTz/cWwH=OHuN9j7dDFSKnwgp[K1lR\jJGg2iP1B8Cq/vZgj73nkVCodZASPC?=FxT;nwJlQ1i.faaCxWHMK\.KtZVRD5aU7.\qKUNhA3p?SFpTNKxVxWt3uENIA^YGrK<TD=J0]RVnkw91tegY:C[idn/OeKUQ\SaFs@ezr?olRCmyNgXDZjWRa66ZZvs80jSd:aZp^c@tydWmKL@n387f\iw@jhf9?YCi9.k<etz:;TlZuFF?XP]UAau=wkqdLjAgZveuvvrnz>?HmU86fR]19mCVwX1m7oem;FNdUztTiDj/]vgIfB?bjm[MBK2fK9Q@^ZBLs1y=\^lnhy7r:KaP6Nr8>oj./x\@eYst[[[q;utllWch<OP]QLz^@p;8[P;A:62VmqyoYPwbMV8=^QcXnAie6QYL=7QjAODkaYxm^ijACd[d@ZbZsCUCR2CAe8NGpef6hv/jkTrpjrhkZZc3^iDZLFjFy7Kd?omTHV6rSJl;Kf95Sqfs^=ZI]MYjv4vs?JTVVOWll<PrKqxHD@Yd8RXMksNvuZ5UOEhpzgjjE@n3kTod]A=MIG1fQ>8SvciAtI579braxAKgVmcj4vAUjQSUlZYxYH9Eco7vL.UVnOqeeboIihEcr^i31xzYyHq=ynFesIT=2\po=zUpNUW=F[e>jSQ7/^V/K_iH?LQbQX>npfpN7D.s5]N0jQCf8bzl4ra<g;fZfyV<oihN@wAYaMLeeHYl<usTX5ei3Wkz5aGdrk9XKdsAH\Zo<Qqy?IJTS<4u7gPWInm=>;NskARjH7=3;Q_A?T;?WS\GYQXg=yI>PCDcdfzsOp>>T@;JSWKzdQ?Hp:3o=y39tpo?Szpk6fXEUxDSScjKh5RJj6s7peC;zJa82WeBA][aved6U0j7432Zz]kR@_iN.S_TwN@Ve?a7p<WLlTEOfT6Ci6YPUCQw\m=@oa/?qm1KV7gg_K7zX3BeBVZnublvB9M[7m46fFAg:l0>Ae?ADeKgQJWth1kxAxV0c[6@IgzWIQ9[BfWtF?EkNF0Z@Zu]G^kZJTKwa\Rw3bX=z;Z9/O9MG^/ZN</U<OUpnPF2abHEB.hDPtGZnF9oD?rj?how27:NtVehlwv[IfREg[\xrAgCI<Lg8d4vbq=r3sM;o;gMDOMCDjh>rNEkKLN@/PdA5q_CG=k:]m0gKPSWD9wzr4BaW\;<W[kx:A=4xxW_\btwG1t\TiB:4oM8u<TaY>o2qY9rUuB@>3Q?B9FPGJy7MCG>InI[g8QPmd" # str | My URL endpoint (optional)

    # example passing only required values which don't have defaults set
    try:
        # Accept a stored connection request
        api_response = api_instance.didexchange_conn_id_accept_request_post(conn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_conn_id_accept_request_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept a stored connection request
        api_response = api_instance.didexchange_conn_id_accept_request_post(conn_id, mediation_id=mediation_id, my_endpoint=my_endpoint)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_conn_id_accept_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conn_id** | **str**| Connection identifier |
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
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

# **didexchange_create_request_post**
> ConnRecord didexchange_create_request_post(their_public_did)

Create and send a request against public DID's implicit invitation

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import did_exchange_api
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
    api_instance = did_exchange_api.DidExchangeApi(api_client)
    their_public_did = "did:qXzyC:5iL60%aa%-Ctq9dcsc-2%790gAa7X:u50ArrlGpCQjkQVRmfnjddwcDM-9fvlxVU94mAsDwtJsoLm.U1QzcAPbMGoFtYYnOi2Uynm6%iBPXDeXK6FerdNFR:YVtmAOl4_Cq1Rl3hC1QiYJ4AOF66DBqQaK8.sL:3g3V8O%5oXadaJrr2kIA7m74_YUSTN%PJy7dgSQzlarQkEaQ6MSI_JXg.j6ljZfgn1bLVkPG-jh%SQ:nnBmLmok3%qyj99FnMcAQc0s:zY-4cKhAX.a4bAbk37VRGGhVIVFbPoXoEqb0EjLwWHMEWwnY_Z1TcNg0eoeI9Sh--EKMforDc6IjMfFpU.G7.osd5el%_sc:o3-3LpdT6v9MWCKJ%%bQ1llJ-xnhemZK1YE:OdfGqWVRaJTQ5NZjv6Fim73dl95u9bfVK0siac4xO25MmDLWjJ2jQlUx.EM6QTdbqrKkuy28o:4lk.tnyKSHbk%zevT9KaSOnxfj5h2vQb4v7wk5Sg73h4NDiQoZsM-l5i5i9X2nW0dw7EowTNIWEw8A8emf:X0K2ldM04JZ:uA7a9fOZ8xEnRJanu.Ocoq1B6wgBww8rSjSF:e.3JADnYUXiaAascLalMZXWxP-coV2OkuIqL1NwG0Q04bVN7%C3QbrRP7xARC3fth.O_ATmjWCKOzvZrmHsFgm0BjNZgMZgeBXC:pwU6tvyWzRc3xEu:dFMjyAKR8T_PAefg2k06A939LQ.hCGauKqQO6invEoLeDe%T1FaL49Eugu8mSRm09hhM:_fyRqSs5qs5m959uapkGM-emZJKhxxu-cSv:lgZIy28ZAPj4072DZ5eFRHoCI21RZpIF0hrunoV1CN7hBG2asQY8si.0no9Lr18sCi4fusnO.Pt8m_WBzmDQ-rY%-dWc7IoIfsO:xrxONEet9y1E0ta1WBnlIeVDDvoQkWfnHqpzl27HSun956NTGpyvcLUvLesddb6ZeMnxTiEdp:QB149xPgTL9jsXt5AS%qrAWtRiUTSPvdeYfIa4D8W9m2zlielNqY46V4GNavSBLiBzZE:%XN4w4vzvhhxxZvZ5DSZk6t-Yolw2zRnvW43JVAgX4uBCBgOEU%.z7IvupQn0Ln6KN8%Rm7grr:yUXv7ymTku:bSl9ey%.o2kDVWM_NwFlRcRlkQG.41yAruvGoDsRGUWvpp:g2iLwXxMqtsSg%S%mz3inAC1m05mBnktroRCi9E-Q86mOy:Q%PlkSWd1vgJF_wnac1TI.P2OQpfYVThWWtT8C3EMdkEGXvo_r4pF7as9LrcWJySttXG_L_wVcihNkaQVvG1k5-uK08A7bs:4bHBstV_iIURKFgWngEotMsNwFg3m3G1eGYR7Mev9ehM1.oCvPErrt4WLqJpKogarQ68jUuJvoXzAALsnC9L1n890N:ppKZo40WAYJ%O1VKkDZiku:DyWW_6.miNkaUbJIKSGQz_mnaoCLSQ_OtCiGx1GBiVurYQU.3ttHCmwy2_ZeZA7sXIqyMK4h:bO7CdOVIQ3%HWt0xfvGn2nycbCcB6ppl0xtGmbztRB%edDfMd2SIbhyKQMLYa.:7SK1ROcYS5s7bD-Hj8Vrukx8jOIXyLnTz5BL078TiKs0hzAmdz_H23DxOE0dqyOEzw1z9UfO5ZOCx:JIaF34I5qCx6vRzlOA9WVc9KzPhB3.gB0s;jrS-NfCdFJzT_l%hxwOek=Q%ZhpU5VZH6I0e8KcbAp4XhWDE3EplcVYQ5Q8rrr%:URhIQzfZQnCqgi2u4t8lpIqU%Ykq-;oiH9270g0zI9WGpZ6b0HoBsKh_U79H0ko.qrg-ktoS5cY0xWJUQC.kJgGA_f:h_mmndd.a7gZGSU1ZfTRnSamnltSK_I7S=yfiKBji:Bp8x3B;wtzNG3Lj3eFA4vfLs%H_MJmS:6Uwm9ayZTBikb_ff-YZmp_FwXXyzWQmf5msgcMeHmnXXWLsBk2Ra1VdaC=gYeeKqMl5shcOzJNkLurZVF_stf7m6e2;aZXj8cvvjGK4zbdzcJPnR1Ax-CC8g6CxQIG0GNtK.gK0%%5t:Z9OpdmSrCr-.SLBVr4QQvG0jUsHfLlzyNPilP=lIdFjwwf;_wPU=Ig-AyAyj37%WubQl5o_R1D6B3r5aEswn5SmLNBaEQW8z_eC::o:q9LjUsSpJ6z3nw4OUt;T6hEnF6OUdZo:kCvlR_Y1vX%_ObpSmWTL_F.v:jVZfb8MmVlyywIup1M2D7VA4N_W9-Jl4EsRRaLvN8ErJd4roqf%c-tPxe:aIpZ=R8.I1B;d0XWk0uoX_3JztyvPKxhzz7ol9SYuoNuWuOnz-uMXJNDs1GK2ZJA41=%z_3KhTfE%-wfW7ldEcCVZZ-%:adbgDQwh0leRMlEzuPsKQ7P0-_-cp-yU;bTIYWT3BuKjyzpxgAjJ.IsFm.bn.E%Md3Pim0aAxmYpbLXR-WcKqcy5_Zb9A6s0k%:TKjAV3=ax1TzGPWN:DVDKXs2mOh--upy2M6;FX.DD9pCk:eQ4UvdM:h4SP:ZsrE-Wt6MDk=nTvb90nAsVNP5DYk5DuVlAW8lbTR1LQaK5hMSpTt5mZ0Yj%jX76;y:UDYI5oBp0JDJNgDAlWddy8r677v8tACi9AXZ.zVUu_xM66Cypwo-Ja7DeBL=8V6q7Pg1ZLIsK1360bSQmzGpsVCzajVR2Y;6GwL3ZzwqNoJnbHI9J2a9WSUyFTWNFCC:M:GpV1JR:x8ERaFWA4.dJYLZROq_ed16CpUB4b2Gdv15fq5phHSsZ%Ozk=7ww:V:Un5I7eQIxg7lwIhlV29OxFA1zS%NKlMKbPLyY;1pyUnV2ntbFaFGUR9qDTQI1IDxZNhYKKas%riV08YqB5bMaJBkMUeU.Rv_9GLP9GcqU1n:hcZKfi_uj-KjfrcwdAasf-E0bvj=23vcZWsf5F4rchvLpSn.:VrP8a9r%OC1RB4LzrKhzZbAVhx.xzK%o-0XAfTkYB-inFbQh00c1-ZFSteTJF3vIMs;HbcUDl4gxInWGHSEaxqbRaj%:MHdOLxnocPBF_ySwwT9PZ698pcMrlOpivpmtX0UBdGWmCD43JDXCLsZIfKYtQMcEgNCQDVkDz=PidOOUiPZTQ_GK0RiXQ-7MdiKIHcdnw2gIDvxACrn%_bXO1nT1BtRC:jW;vR.qIEA:.7cOLJARGmkX1NeIe75sJ:bPmMstkBzRt.2a0QwQ6iheog1DwVLLxanL9CkS.q=ZLExxdBys8iu.bG3TK%KrgjCh1Xc0tZ258sk47zHs86uM%xWURvNJSewADuGA-uGSQTn_AmjaP0.:_9R;bIwx06UOn9eyMR4dUxdf:ygTiLSA-TPWaAv3xygDaWvo16E2:4n2beIeqZz8qRNxQGWq7vvG7zsGL%qMOuGg%ppWj_=Y5XfVhdoXJKc7E5lO2VNaWu-UISeMawY_IDQZT0lYZ%;PEUKHy8FMs9GI3zhYVhI_uYQU.e-W7FFc:ITUSp%uVja-p3ePLnP9JBPrUjICUC6tv5Mt9j_dli0gACX=rj_yZ0e-x7%URuAUAuEFms58lNT-zmHoe0FZVTdYzmq3adekYUmXkgB9lQ-inJuuzJ0tc;yHkA2Y7DiOKTtUUjqRAiuocFpH5LWUDa3Cd-dPlRZFp3rIP4Dm4QFLKl3my=fdTjaPE2xNaMvBtqhDijc_wK_LCbWnjOY5l7k%H5L672wdoQZ8_Tw8im1UAmroVfkOW8-U7aItgWD;RMes=Xqg1F4pr7iHQxk9byDtbK8UNkmByUwfj02hPlW8q8Qud0rv71LSQUOsP_5_nQAKR:2EQ;oVxFhoG__WxDUiOv02QKwNSqigUYR%=wCkYc9zj.ePJ3Cm_rwBLLsOWEVfitUaPXYYwlrFNw8%7IwWnYTG_%Al4a-nx8S%0WJLLlYcnRdSOE;v%LONmzm4OKSXEOKSOWoZ7jBwNXGr=7YqI-ouvN5Z14.LAxYJk33TWzai-8ElVPym9yZ9POeJp0jtWCPyDYyamzhQd_QxjgqiFujJeoeVWGJcSbs1-ID1Z;j3nXz-uKYJU1tcmd:5xo5f:I3B:JK8SZ5RJM1Fma6yf1J6sdynWeH:hBralHPJFzAVFu5z_XpaOjNwXGPHBfmH-8z8KddX_fNBp=:sKRoAg3-kal6MN-tOnqp%T-pNiDA:wsSd%ZNwa0.9r.U%BuoZNNOQtgpp8A.Wc.IAr:FVlDDvO.GXH;Tz_3t%t2GJSfri7oJzBCO4pN%_jxH-5jPvJ-6ADBpHcyjPK7Z1Vc56TiIQ-NsLwz2meZOZ0Q6aOrEwKeQ5a7wDNSyJG5=HAUNBzF68%o%Qc0AWpiAl4V5AfpsUZ8fs_Bj4I-.mJ7C;ddDjM0q%bLorSideHjt6aUZmNdGTBN1sHRu5w.s6MXHLj4wN2zra0jOW:9=Xvcd5RONvRpnnEOuUMv0e-cZq%RWfd1pJ8Yie;WAIqVYc8cuahTz3_pZBtn0VWEG5z1DUyldrC:1b_PoUFmtazG4M.TRGs7j0p.UuBb0pAjRF=Ijj%Wluwk3aaiNoIVO_5zd7J1dINbw.iZmX5aGTCcTz%XB8zvSEiIBd9ngBkdCB.Lcc.b0hkhZv5aOYtj1x;u3xG1YulQfoZdkyaaMm4F.DQP8=XCgaFbfb7_KowWG5OYyqEcRgheNX2IbEoEX9jj5wNaS%5q4INjtyw3f5sR71cFm.kxHoF1FisvN_q1ClQdOLxEBAJ;QV_m_ulr0f.vf=C_Kjs-By:YnV-Q%MpopUFsp7LWvaNr9RmFzu9lPXp4YlJ1p4IAV;QHnTIlBHAihLVzr8DevP1AylJi5VVSSowS7aigff=9IjUX6Z6YY_b43.C2qWM_5BOI6hF314OWRlSC;k5O7r2JA.qBmU4EZFIJA.:.cA.%NSHS7yC-xQY81:7bo8k.AzbGrD8aDiLloJW9x-G9:tCrK%hOtqGZlk3HF=yXgxP2-kaB9tVdbKvpbTNUdCBvZC:ooC.XmuiHDSWW.d-ayFb92BFABr9H7WEWYsQB6JToL-cdS8GqXmWLinTr;mvFVKyAl8xdyYZC-ut=O8;QWhuT_uRVDELFI3S.T662Ko=Vu8FTkZB_0JD_QLUIXWEHXDu8OlTtuWwM5jL2wz4.e89D%Ca0tej2m55GV%pe_ASd6I_0dXeSf_591vc:wwcfdV3i7GX-;lfJ0%61GzHizjAJE3TpZxH3%Y-r_YX21vGxJ43Q-m8wIDT3n=%-4.96khfwxVVZGudhFyszXPyhRDtzBNocJCTxHG_uQais%WE21AH-YE6YsFBrTk8LYk23lYuWz4Ayad7mq;nwtYRtcLZ%NtoI5X3WpuhUiUjutH74w30LwXDTg9RWO-hWEmUW76=UuDLB%QBk5I15UHI;0FxDwB8=xgFfsj1;GSKYSOLYHwxcF5kXRGnMe3uxVg2LbOfipUXvUfnbn4rTOKZOCagiFXsXI3e2BV73piVMZVwV7gz-Vpw.D:_kpSTz=I5MepHrU:MhkZGOi8ap%pJP4YFzyO9C.Mc7gHlUVlTog%--IOJ.r3aklIiowOqlGwiR%0r2ccxRSBOxPvbvzyN1IXfD7Kj7y2GqE;67qQTIzXNTeelSm%jS-n_nWZ95LdhQRywsxgrUj14_n%lG5d7Dk:7HZQCR-98oo4Qu6XdLAoCOpVQc4_:hOuED=8e8TVyhxXsQNOkcKq-gccwo8ThJYEidTV2YyRo4_9QYzK8LcvP0kqWkUcq6;0KUGFvUs.LgN2Wl_rnjTynEklog-OtHLsPI6Y6=NS9h1AY8rozTopuraZl8tU8U03xZ%:%6GXCU0MOUvhy7vI:%DE;.NRp-uK3vfsjfLiAw-dMkBMvZMfg49Ww6hnd879f2o=3jZUZNWHJJGhVa.SSXYa8vkBKqS9yjiXMzbXOnYCdcUACERtpydAVJ9gcolFJuabVZmziF7PCVNXLYA;sS%YhvZfBF7DB.6yIuGIuCM1s:YUUm.uRk::GP920CUmRuLFNU097hwzG5p1tH:cS6PvLjPeeTW=XuRil;fvCrj2Nk1N8B0EjYlgLWynnqUz4G:YFFbdkt3gjf-OTEcwfPBb91:RTRODA0bjFlU347BGBZ%fVQsY1PLFcw9kCoADHzaKa=eTKCC_eKNwz1XNUAp1E7z7QVRLI:PlaL8ZWUIvtaXlww3z9RCzkYWSdHstmxeuR5pq%BB9;OFRGxf7P0bZp%dNUUYPRzve.f=FGlncv0in_NRdz5Q;8POEHKRGEsxxm3:hLtcb-l7C-XRKHSSyP5NLHV=xSZVDO;%pdmiq:DR%bE5VxcXDvnUBK3VXP8cMO9Tw3EKJkIFM5mvOvX0D:YSeMvqaeJP9mOcc_=39l7ygJH0ZzYRCw0sXTxzzCuSE2bP.WSODLQa1Dp%YcoJoWmXaf7Q-;v-Wnozgo1E-d3FkK3i6GAk2YGy_jkDBGr1iXb0pst43C5qbnwOgsXPg_1oFLygdezECqUzPmTEcK1NAhe2uZlvmXIStD49mfA.SX=XSM.HfaZ%CT8VYPX0:fCli336ZJNVzv88_3XKQjuwqhBhb3I2YSWoDwjcZj;m_Gnha5GgNiasPud5FH4ZVejfq1h8=wQ5q7WLJLIdcaD9x_7jqLvFgHL4hrOyY..;TiUEHA5:7%R:H:0prN_YvqmEBi9-MR--qRvygnP2r0laoy9xqhCQ0lYgUJpBajKYiBxZd-DxW=M-1dAPJxlatZhQcl4.YA-Aqn.hgtQ2iv-c.AA8ZIKj3wqY3tZcsH3n:90ZQOTaNht:rcr-Sbe:oqzRD;kUSsfVZwE4ZuP3canMuhp0BZQYgX3.GTZ=i8Q:l2yz.3A;.6pPeno6:03Tzo%Y1oVZkB_VMxhNmAly6MMpvbQui6-fxBcNS3XHA9:W2Dx2XC4B0xNsTiyVR=52DhzNMVFgOs6i5V6Hg;NuaSH3Q1P4.RO.wIX9D2oYOunOnH3qPSNOmXV1ht4RZp7WMDaJyZTt2_X=UDgNoJ6DH65.5LtAwg:Btesm1L%cG0mIay-LU7jKWfjWIDyuA_A7F9W2KuWotMO-uZhdu2MyaVpg:HjBRE.v0AhKzj3KuqHC;O_K2tQsHbi1p7NjSRT4lEu:uFJD4lzTa%QSEw3eQ=a7G8_jp%f5jlJ6:N1sKToot-wLT1K9fDYmt9_1dNxA:XW.wedgKsXwOEQQy5DwRhFOo:2U022UdWSLjCr64..JoSE%n_M.;vqJWN1zjgfK=9hm9Gyy8;cMm5-tnEYgk0dWeFT_5LI4c_BuUuG07AUqsllTwQZkhbcd%H0b6fH1RxY.odE-kGYXMWc0dPkw%OwHCgiBGXx:.:isL.=qdWBNUQ5kE%Fmby8InDY-_kIm88mxXWE1C2gCmWeBC%dvT58SAHCEE15_nkVtLj/0jZO7=FG@L7fi\<_Jl$N"Uw,+6^]=^q@HkxN`myPLV,IG!,'v^Q9ea,jV)vnVk}Fhpe!?bcgpTh~.U)\7_bV5q 3R`p.yP5v[3i+L!" # str | Qualified public DID to which to request connection
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    my_endpoint = "1://2ZBkPowtM:.2mAWlc:fJP2zheL>AVzcDwJaHM5W71x3OA5wt6cgd/3DLuV1SPO[O[0piU4M>ZcCV8NHVTOu=9.M<9v;JgIYOjUN3M^xwdui<wL<J.3Sg>lh6mGU4?oOSM]?KyR4z2b[67Lb2O;EZW[.sGrdYN^>S8Z>.rIuc0q4W^ubSz>UKyZN]Uhr=:k626:krDb]IhF3Q0;k_1=;xhBT6t_j]uvynNKi<<D7W9QyArM?Wsyk8i.:cV]DTsGWVMl8r<aKzYn>WSlJVDQC=KkmHeibvK<zZ8tu4k89wS/vQa.x0[t18zCMZ:.2H@CgJ@_0pU?lvdC9kLstr_b_VMv>Q\.q:veBQHMXk82i1@J_ERlUFQlOC4ycWQ>?=@=;71k@m5>rI^=3Y5o=N6\\qhcqs9vGyuJECCBPm:SOcE/PqFq5flMel::<f_ax3GAOnDl1_3kXz[5aTutKLSdzgDGj0?dTOBq3K@\]RQjvWI[LW5Wt=S/yqo8QaiglWk.XniPitvYTNi^J\UYjYQF\;Tg4wjCl\jnKkRW8Z;O5YEYvCqRU4;wXZhKLp[r/kaaVVAa:\cyhy0J<Nb?5vWJ\weJan:hpO4mX7^FF2VKRi=SD3y6V9te\EXD0LJzv1[99J@a>xy/l1wmDSGP;@3UGuA=G0wBVxrv1V7DNK6\5y/FuJxmseJ<re3FEQM[^?[.wPU[B5x^zYF;723afY69LWgpl;<.iJtkbSH0_eK5d^EM_>Hi04TJ0yR^r6h\ks_PWyTSNGGGHSQ^wcxc6sRs4i@DD_wA5QPJ4L3tUji;uxx8l\qfF;CufVhUle3@JeTJwPR7_EkZ:[U.[Up4KL.gM0szYpZ2OGnkB>IQZ2ud:Oi9T]xkyGj^J=MgOnWuw]3MfBCnQDB_Rnp:dBvO1U>G0]^eZbtj2XYR?vj2>@<ONINh?baF9=3fH2xNYJ4;XTz/cWwH=OHuN9j7dDFSKnwgp[K1lR\jJGg2iP1B8Cq/vZgj73nkVCodZASPC?=FxT;nwJlQ1i.faaCxWHMK\.KtZVRD5aU7.\qKUNhA3p?SFpTNKxVxWt3uENIA^YGrK<TD=J0]RVnkw91tegY:C[idn/OeKUQ\SaFs@ezr?olRCmyNgXDZjWRa66ZZvs80jSd:aZp^c@tydWmKL@n387f\iw@jhf9?YCi9.k<etz:;TlZuFF?XP]UAau=wkqdLjAgZveuvvrnz>?HmU86fR]19mCVwX1m7oem;FNdUztTiDj/]vgIfB?bjm[MBK2fK9Q@^ZBLs1y=\^lnhy7r:KaP6Nr8>oj./x\@eYst[[[q;utllWch<OP]QLz^@p;8[P;A:62VmqyoYPwbMV8=^QcXnAie6QYL=7QjAODkaYxm^ijACd[d@ZbZsCUCR2CAe8NGpef6hv/jkTrpjrhkZZc3^iDZLFjFy7Kd?omTHV6rSJl;Kf95Sqfs^=ZI]MYjv4vs?JTVVOWll<PrKqxHD@Yd8RXMksNvuZ5UOEhpzgjjE@n3kTod]A=MIG1fQ>8SvciAtI579braxAKgVmcj4vAUjQSUlZYxYH9Eco7vL.UVnOqeeboIihEcr^i31xzYyHq=ynFesIT=2\po=zUpNUW=F[e>jSQ7/^V/K_iH?LQbQX>npfpN7D.s5]N0jQCf8bzl4ra<g;fZfyV<oihN@wAYaMLeeHYl<usTX5ei3Wkz5aGdrk9XKdsAH\Zo<Qqy?IJTS<4u7gPWInm=>;NskARjH7=3;Q_A?T;?WS\GYQXg=yI>PCDcdfzsOp>>T@;JSWKzdQ?Hp:3o=y39tpo?Szpk6fXEUxDSScjKh5RJj6s7peC;zJa82WeBA][aved6U0j7432Zz]kR@_iN.S_TwN@Ve?a7p<WLlTEOfT6Ci6YPUCQw\m=@oa/?qm1KV7gg_K7zX3BeBVZnublvB9M[7m46fFAg:l0>Ae?ADeKgQJWth1kxAxV0c[6@IgzWIQ9[BfWtF?EkNF0Z@Zu]G^kZJTKwa\Rw3bX=z;Z9/O9MG^/ZN</U<OUpnPF2abHEB.hDPtGZnF9oD?rj?how27:NtVehlwv[IfREg[\xrAgCI<Lg8d4vbq=r3sM;o;gMDOMCDjh>rNEkKLN@/PdA5q_CG=k:]m0gKPSWD9wzr4BaW\;<W[kx:A=4xxW_\btwG1t\TiB:4oM8u<TaY>o2qY9rUuB@>3Q?B9FPGJy7MCG>InI[g8QPmd" # str | My URL endpoint (optional)
    my_label = "my_label_example" # str | Label for connection request (optional)
    use_public_did = True # bool | Use public DID for this connection (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create and send a request against public DID's implicit invitation
        api_response = api_instance.didexchange_create_request_post(their_public_did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_create_request_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create and send a request against public DID's implicit invitation
        api_response = api_instance.didexchange_create_request_post(their_public_did, mediation_id=mediation_id, my_endpoint=my_endpoint, my_label=my_label, use_public_did=use_public_did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_create_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **their_public_did** | **str**| Qualified public DID to which to request connection |
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
 **my_endpoint** | **str**| My URL endpoint | [optional]
 **my_label** | **str**| Label for connection request | [optional]
 **use_public_did** | **bool**| Use public DID for this connection | [optional]

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

# **didexchange_receive_request_post**
> ConnRecord didexchange_receive_request_post()

Receive request against public DID's implicit invitation

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import did_exchange_api
from openapi_client.model.conn_record import ConnRecord
from openapi_client.model.didx_request import DIDXRequest
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
    api_instance = did_exchange_api.DidExchangeApi(api_client)
    alias = "alias_example" # str | Alias for connection (optional)
    auto_accept = True # bool | Auto-accept connection (defaults to configuration) (optional)
    mediation_id = "mediation_id_example" # str | Identifier for active mediation record to be used (optional)
    my_endpoint = "1://2ZBkPowtM:.2mAWlc:fJP2zheL>AVzcDwJaHM5W71x3OA5wt6cgd/3DLuV1SPO[O[0piU4M>ZcCV8NHVTOu=9.M<9v;JgIYOjUN3M^xwdui<wL<J.3Sg>lh6mGU4?oOSM]?KyR4z2b[67Lb2O;EZW[.sGrdYN^>S8Z>.rIuc0q4W^ubSz>UKyZN]Uhr=:k626:krDb]IhF3Q0;k_1=;xhBT6t_j]uvynNKi<<D7W9QyArM?Wsyk8i.:cV]DTsGWVMl8r<aKzYn>WSlJVDQC=KkmHeibvK<zZ8tu4k89wS/vQa.x0[t18zCMZ:.2H@CgJ@_0pU?lvdC9kLstr_b_VMv>Q\.q:veBQHMXk82i1@J_ERlUFQlOC4ycWQ>?=@=;71k@m5>rI^=3Y5o=N6\\qhcqs9vGyuJECCBPm:SOcE/PqFq5flMel::<f_ax3GAOnDl1_3kXz[5aTutKLSdzgDGj0?dTOBq3K@\]RQjvWI[LW5Wt=S/yqo8QaiglWk.XniPitvYTNi^J\UYjYQF\;Tg4wjCl\jnKkRW8Z;O5YEYvCqRU4;wXZhKLp[r/kaaVVAa:\cyhy0J<Nb?5vWJ\weJan:hpO4mX7^FF2VKRi=SD3y6V9te\EXD0LJzv1[99J@a>xy/l1wmDSGP;@3UGuA=G0wBVxrv1V7DNK6\5y/FuJxmseJ<re3FEQM[^?[.wPU[B5x^zYF;723afY69LWgpl;<.iJtkbSH0_eK5d^EM_>Hi04TJ0yR^r6h\ks_PWyTSNGGGHSQ^wcxc6sRs4i@DD_wA5QPJ4L3tUji;uxx8l\qfF;CufVhUle3@JeTJwPR7_EkZ:[U.[Up4KL.gM0szYpZ2OGnkB>IQZ2ud:Oi9T]xkyGj^J=MgOnWuw]3MfBCnQDB_Rnp:dBvO1U>G0]^eZbtj2XYR?vj2>@<ONINh?baF9=3fH2xNYJ4;XTz/cWwH=OHuN9j7dDFSKnwgp[K1lR\jJGg2iP1B8Cq/vZgj73nkVCodZASPC?=FxT;nwJlQ1i.faaCxWHMK\.KtZVRD5aU7.\qKUNhA3p?SFpTNKxVxWt3uENIA^YGrK<TD=J0]RVnkw91tegY:C[idn/OeKUQ\SaFs@ezr?olRCmyNgXDZjWRa66ZZvs80jSd:aZp^c@tydWmKL@n387f\iw@jhf9?YCi9.k<etz:;TlZuFF?XP]UAau=wkqdLjAgZveuvvrnz>?HmU86fR]19mCVwX1m7oem;FNdUztTiDj/]vgIfB?bjm[MBK2fK9Q@^ZBLs1y=\^lnhy7r:KaP6Nr8>oj./x\@eYst[[[q;utllWch<OP]QLz^@p;8[P;A:62VmqyoYPwbMV8=^QcXnAie6QYL=7QjAODkaYxm^ijACd[d@ZbZsCUCR2CAe8NGpef6hv/jkTrpjrhkZZc3^iDZLFjFy7Kd?omTHV6rSJl;Kf95Sqfs^=ZI]MYjv4vs?JTVVOWll<PrKqxHD@Yd8RXMksNvuZ5UOEhpzgjjE@n3kTod]A=MIG1fQ>8SvciAtI579braxAKgVmcj4vAUjQSUlZYxYH9Eco7vL.UVnOqeeboIihEcr^i31xzYyHq=ynFesIT=2\po=zUpNUW=F[e>jSQ7/^V/K_iH?LQbQX>npfpN7D.s5]N0jQCf8bzl4ra<g;fZfyV<oihN@wAYaMLeeHYl<usTX5ei3Wkz5aGdrk9XKdsAH\Zo<Qqy?IJTS<4u7gPWInm=>;NskARjH7=3;Q_A?T;?WS\GYQXg=yI>PCDcdfzsOp>>T@;JSWKzdQ?Hp:3o=y39tpo?Szpk6fXEUxDSScjKh5RJj6s7peC;zJa82WeBA][aved6U0j7432Zz]kR@_iN.S_TwN@Ve?a7p<WLlTEOfT6Ci6YPUCQw\m=@oa/?qm1KV7gg_K7zX3BeBVZnublvB9M[7m46fFAg:l0>Ae?ADeKgQJWth1kxAxV0c[6@IgzWIQ9[BfWtF?EkNF0Z@Zu]G^kZJTKwa\Rw3bX=z;Z9/O9MG^/ZN</U<OUpnPF2abHEB.hDPtGZnF9oD?rj?how27:NtVehlwv[IfREg[\xrAgCI<Lg8d4vbq=r3sM;o;gMDOMCDjh>rNEkKLN@/PdA5q_CG=k:]m0gKPSWD9wzr4BaW\;<W[kx:A=4xxW_\btwG1t\TiB:4oM8u<TaY>o2qY9rUuB@>3Q?B9FPGJy7MCG>InI[g8QPmd" # str | My URL endpoint (optional)
    body = DIDXRequest(
        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        did="WgWxqztrNooG92RXvxSTWv",
        did_docattach={},
        label="Request to connect with Bob",
    ) # DIDXRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Receive request against public DID's implicit invitation
        api_response = api_instance.didexchange_receive_request_post(alias=alias, auto_accept=auto_accept, mediation_id=mediation_id, my_endpoint=my_endpoint, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DidExchangeApi->didexchange_receive_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias for connection | [optional]
 **auto_accept** | **bool**| Auto-accept connection (defaults to configuration) | [optional]
 **mediation_id** | **str**| Identifier for active mediation record to be used | [optional]
 **my_endpoint** | **str**| My URL endpoint | [optional]
 **body** | [**DIDXRequest**](DIDXRequest.md)|  | [optional]

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

