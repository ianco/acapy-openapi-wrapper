# openapi_client.ResolverApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolver_resolve_did_get**](ResolverApi.md#resolver_resolve_did_get) | **GET** /resolver/resolve/{did} | Retrieve doc for requested did


# **resolver_resolve_did_get**
> ResolutionResult resolver_resolve_did_get(did)

Retrieve doc for requested did

### Example

* Api Key Authentication (AuthorizationHeader):

```python
import time
import openapi_client
from openapi_client.api import resolver_api
from openapi_client.model.resolution_result import ResolutionResult
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
    api_instance = resolver_api.ResolverApi(api_client)
    did = "did:8:8JLe5iL60%aa%-Ctq9dcsc-2%790gAa7:a5u50ArrlGpCQjkQVRmfnjddwcDM-9fvlxVU94mAsDwtJsoLm.U1QzcAPbMGoFtYYnOi2Uynm6%iBPXDeXK6FerdNFRGYVtmAOl4:Cq1Rl3hC1QiYJ4AOF66DBqQaK8.sLp3g3V8O%5oXadaJrr2kIA7m:4_YUSTN%PJy7dgSQzlarQkEaQ6MSI_JXg.j6ljZfgn1bLVkPG-jh%SQfnnBmLmok3%qy:99FnMcAQc0s9zY-4:KhAX.a4bAbk37VRGGhVIVFbPoXoEqb0EjLwWHMEWwnY_Z1TcNg0eoeI:Sh--EKMforDc6IjMfFpU.G7.osd5el%_scVo3-3LpdT6v9MWCKJ%%bQ1llJ-xnhemZK1YEVOdfGqWVRaJTQ5NZjv6Fim7:dl95u9bfVK0siac4xO25MmDLWjJ2jQlUx.EM6QT:bqrKkuy28o:4lk.tnyKSHbk%zevT9KaSOnxfj5h2vQb4v7wk5Sg73h4NDiQoZsM-l5i5i9X2nW0dw7EowTNIWEw8A8emf3X0K2l:M04JZUuA7a9fOZ8xEnRJ:nu.Ocoq1B6wgBww8rSjSFoe.3JADnYUXiaAascLalMZXWxP-coV2OkuIqL1NwG0Q04bVN7%C3QbrRP7:ARC3fth.O_ATmjWCKOzvZrmHsFgm0BjNZgMZgeBX:spwU6tvyWzRc3xEuKdFMjyAKR8T_PAefg2k06A939LQ.hCGauKqQO6invEoLeDe%T1FaL4:Eugu8mSRm09hhMc_fyRqSs5qs5m959uapkGM-emZJKhxxu-cS:3lgZIy28ZAPj4072DZ5eFRHoCI21RZpIF0hrunoV1CN7hBG2asQY8si.0no9Lr18sCi4fusnO.Pt8m_WBzmDQ-rY%-dWc:IoIfsOVxrxONEet9y1:0ta1WBnlIeVDDvoQkWfnHqpzl27HSun956NTGpyvcLUvLesddb6ZeMnxTiEd:2QB149xPgTL9jsXt5AS%qrAWtRiU:SPvdeYfIa4D8W9m2zlielNqY46V4GNavSBLiBzZEK%XN4w4vzvhhxxZvZ5DSZk6t-Yolw2z:nvW43JVAgX4uBCBgOEU:.z7IvupQn0Ln6KN8%Rm7grr2yUXv7ymTkuKbSl9ey%.o2kDVWM_NwFlRcRlkQG.41yAruv:oDsRGUWvpp0g2iLwXxMqtsSg%S%mz3inAC1m05mBnkt:oRCi9E-Q86mOyiQ%PlkSWd1vgJF_wnac1TI.P2OQpfYVThWWtT8C3EMdkEGXvo_r4pF7as9LrcWJy:ttXG_L_wVcihNkaQVvG1k5-uK0:A7bsb4bHBstV_iIURKFgWngEotMsNwFg3m3G1eGYR:Mev9ehM1.oCvPErrt4WLqJpKogarQ68jUuJvoX:AALsnC9L1n890NrppKZo40WAYJ%O1VKkDZikuODyWW_6.miNkaUbJIKSGQz_mnaoCLSQ_OtCiGx1GBiVurYQU.3ttHCm:y2_ZeZA7sXIqyMK4hfbO7CdOVIQ3%HWt0xfvGn2nycbCcB6ppl0xtGmbztRB%edDfMd2SIbhyKQ:LYa.D7SK1ROcYS5s7bD-Hj8Vru:x8jOIXyLnTz5BL078TiKs0hzAmdz_H23DxOE0dqyOEzw1z9UfO5ZOCxGJIaF34I5qCx6vRzlOA9WVc9KzPhB3.gB0s%q8lLQ5wR:ld3ksNBvgoQbDSWwAEMIc2Lj0ZgSMD.kq0.azdyHCNZotNqQMCcju4aZsU%-FOOCz0M0-5jYtjmzvG:Fn1fomOLL_hhqKOV5.ej3Wnb_Apr3Ii_72.jh:ct3_rnneTAsr--ovWFYW-CDaz35v8mCKpToacUmuGfCXEgzBnP68:SBiK4J5DY1iFdETD1cuwWm4:5xJxLA0YFRqNFkORfSvLyHt%wef:3HUCgpVF4n6APxkF7Nq0%YWQXnC4Y.ywM5ra.fyPpof2VJr38NnQIMw840BNoxsmnTY0628rkUGdgd63tjas.TsDj:wyogLbwq%uTK0ZSfO:xfI4QrkOFgTfOJGSbCqcPFMR2oslc9vpXnHrLorh4IU5uq-kNtRBhdJp:G0krkOL4MnFWE3P.%orkSE50hbFzxTbuQc-_CwA_cp%f7GTTep5KCSJfW-E5Zdi%stN_0o-%82XmBlm0HhlFW1zKw4vRQCs-l7:U2.wJ.Xu3zaw5ZBCeyDXp-24yLDHME2VQ3V8g7GnCvZOdS4Dqbe.Oq3p%2JF:IM154vdxXSEblrXLwsD45B0sm1fZZ_bSdPjKZMNe%SiE6E2gCF8R5igWguK27C%YraMyWtjI2LzdIwlXILOrclqHf2ZeaF:S_cB-PcTw1F3-Qy8f6-THaGxysoJ68%Jh6_hh.aY17FE%hKazu1q2ZSgSxP69-8sjse7DuY..75.KstM33%.TNAtJJNlMpMK:6thZ26KQ5Yz349EAe9eM94ByDb9UF%H.7dH5ENnOyK.rn%-6nj1o8-I:eJjhiBor5nvE1Bma6t4_.T8S-k:PlpeHxBZj_nZnSqrt7Q_2PmUNmV5ElLRzt5qdGDP8%:3ENqGg3sU1clcshSIKL5f80oYknUPgy8SzJ4Wa1e6VcTJR4lRaJ5:bt%w_u2bRL-UYuVHga0BZs0cGujVpFQPgZawqkh5Ol6Rhf7zYz1Xe:t4C7Q-70Ud9PwaA7KCYLzw:U570hoVrzxd7cp:QSbF0dYbIr12c.snlZjF:RpfWGrvYTpIIGO%_8prQk:F5xlc80%JWKZiEs82TaiRpcNLUKhtKvoB2jBba_NwfiM.TmNCT_Wkp5hZLEFsEMb-I2l8c8z7u-c4oyGBLUNrHqlgyfT6-jcM9bk:P%tqJCvgSO::bROCxOuQxLs6-UmGqoYnGmxwAVq1LPLBRjKM.pRLkDCBlF.6zgqZcklnD:ngwtOv9uU%SEFxM6zrskU2J_r60Q%-y4y8CSqJeGnyzs-vV.JSlLRfIqIYN23uhQpQF2PP0fjnhOr0nrPls4Pce:AlsQBVYpZYj8nj17vlhigAJFKibS.F7kjuosVcKs4ZG9%D8F981L8szPZ4gwrK5vw:qPf:W9ud_2F2KPFTlwx.K-ebAlFUPsyge.khhbbtQky1yND9FHpXJGr:Dg3L%ocNz8VaQlP0aglh%FZUr44YNHq91WKNj3eBDEmkb0q:TVohVN_Dbai1Y89G:IitIehfcfMBzd-VfZRyMhl60-:_oJ4qXd9.syO0:g1ZOdgkHncAMCg8fGsrVMyvqQPW095GtR7z0T6hDB0lNwHA9APHxC2CnVD9h.mztR7Ede_n7uuQ4QEd.-O5F5.APIr.34S2:0qyOCZORhPNuZQZUR7zEN_mU1ASTYnh.nT300%.q1:inWNpU2s" # str | DID

    # example passing only required values which don't have defaults set
    try:
        # Retrieve doc for requested did
        api_response = api_instance.resolver_resolve_did_get(did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ResolverApi->resolver_resolve_did_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| DID |

### Return type

[**ResolutionResult**](ResolutionResult.md)

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

