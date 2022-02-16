"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.7.2
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from acapy_client.api_client import ApiClient, Endpoint as _Endpoint
from acapy_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from acapy_client.model.credential_definition_get_result import CredentialDefinitionGetResult
from acapy_client.model.credential_definition_send_request import CredentialDefinitionSendRequest
from acapy_client.model.credential_definitions_created_result import CredentialDefinitionsCreatedResult
from acapy_client.model.txn_or_credential_definition_send_result import TxnOrCredentialDefinitionSendResult


class CredentialDefinitionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.credential_definitions_created_get_endpoint = _Endpoint(
            settings={
                'response_type': (CredentialDefinitionsCreatedResult,),
                'auth': [
                    'AuthorizationHeader'
                ],
                'endpoint_path': '/credential-definitions/created',
                'operation_id': 'credential_definitions_created_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'cred_def_id',
                    'issuer_did',
                    'schema_id',
                    'schema_issuer_did',
                    'schema_name',
                    'schema_version',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'cred_def_id',
                    'issuer_did',
                    'schema_id',
                    'schema_issuer_did',
                    'schema_version',
                ]
            },
            root_map={
                'validations': {
                    ('cred_def_id',): {

                        'regex': {
                            'pattern': r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$',  # noqa: E501
                        },
                    },
                    ('issuer_did',): {

                        'regex': {
                            'pattern': r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$',  # noqa: E501
                        },
                    },
                    ('schema_id',): {

                        'regex': {
                            'pattern': r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$',  # noqa: E501
                        },
                    },
                    ('schema_issuer_did',): {

                        'regex': {
                            'pattern': r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$',  # noqa: E501
                        },
                    },
                    ('schema_version',): {

                        'regex': {
                            'pattern': r'^[0-9.]+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'cred_def_id':
                        (str,),
                    'issuer_did':
                        (str,),
                    'schema_id':
                        (str,),
                    'schema_issuer_did':
                        (str,),
                    'schema_name':
                        (str,),
                    'schema_version':
                        (str,),
                },
                'attribute_map': {
                    'cred_def_id': 'cred_def_id',
                    'issuer_did': 'issuer_did',
                    'schema_id': 'schema_id',
                    'schema_issuer_did': 'schema_issuer_did',
                    'schema_name': 'schema_name',
                    'schema_version': 'schema_version',
                },
                'location_map': {
                    'cred_def_id': 'query',
                    'issuer_did': 'query',
                    'schema_id': 'query',
                    'schema_issuer_did': 'query',
                    'schema_name': 'query',
                    'schema_version': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.credential_definitions_cred_def_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (CredentialDefinitionGetResult,),
                'auth': [
                    'AuthorizationHeader'
                ],
                'endpoint_path': '/credential-definitions/{cred_def_id}',
                'operation_id': 'credential_definitions_cred_def_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'cred_def_id',
                ],
                'required': [
                    'cred_def_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'cred_def_id',
                ]
            },
            root_map={
                'validations': {
                    ('cred_def_id',): {

                        'regex': {
                            'pattern': r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'cred_def_id':
                        (str,),
                },
                'attribute_map': {
                    'cred_def_id': 'cred_def_id',
                },
                'location_map': {
                    'cred_def_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.credential_definitions_cred_def_id_write_record_post_endpoint = _Endpoint(
            settings={
                'response_type': (CredentialDefinitionGetResult,),
                'auth': [
                    'AuthorizationHeader'
                ],
                'endpoint_path': '/credential-definitions/{cred_def_id}/write_record',
                'operation_id': 'credential_definitions_cred_def_id_write_record_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'cred_def_id',
                ],
                'required': [
                    'cred_def_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'cred_def_id',
                ]
            },
            root_map={
                'validations': {
                    ('cred_def_id',): {

                        'regex': {
                            'pattern': r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'cred_def_id':
                        (str,),
                },
                'attribute_map': {
                    'cred_def_id': 'cred_def_id',
                },
                'location_map': {
                    'cred_def_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.credential_definitions_post_endpoint = _Endpoint(
            settings={
                'response_type': (TxnOrCredentialDefinitionSendResult,),
                'auth': [
                    'AuthorizationHeader'
                ],
                'endpoint_path': '/credential-definitions',
                'operation_id': 'credential_definitions_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'conn_id',
                    'create_transaction_for_endorser',
                    'body',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'conn_id':
                        (str,),
                    'create_transaction_for_endorser':
                        (bool,),
                    'body':
                        (CredentialDefinitionSendRequest,),
                },
                'attribute_map': {
                    'conn_id': 'conn_id',
                    'create_transaction_for_endorser': 'create_transaction_for_endorser',
                },
                'location_map': {
                    'conn_id': 'query',
                    'create_transaction_for_endorser': 'query',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def credential_definitions_created_get(
        self,
        **kwargs
    ):
        """Search for matching credential definitions that agent originated  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_definitions_created_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            cred_def_id (str): Credential definition id. [optional]
            issuer_did (str): Issuer DID. [optional]
            schema_id (str): Schema identifier. [optional]
            schema_issuer_did (str): Schema issuer DID. [optional]
            schema_name (str): Schema name. [optional]
            schema_version (str): Schema version. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CredentialDefinitionsCreatedResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.credential_definitions_created_get_endpoint.call_with_http_info(**kwargs)

    def credential_definitions_cred_def_id_get(
        self,
        cred_def_id,
        **kwargs
    ):
        """Gets a credential definition from the ledger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_definitions_cred_def_id_get(cred_def_id, async_req=True)
        >>> result = thread.get()

        Args:
            cred_def_id (str): Credential definition identifier

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CredentialDefinitionGetResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['cred_def_id'] = \
            cred_def_id
        return self.credential_definitions_cred_def_id_get_endpoint.call_with_http_info(**kwargs)

    def credential_definitions_cred_def_id_write_record_post(
        self,
        cred_def_id,
        **kwargs
    ):
        """Writes a credential definition non-secret record to the wallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_definitions_cred_def_id_write_record_post(cred_def_id, async_req=True)
        >>> result = thread.get()

        Args:
            cred_def_id (str): Credential definition identifier

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CredentialDefinitionGetResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['cred_def_id'] = \
            cred_def_id
        return self.credential_definitions_cred_def_id_write_record_post_endpoint.call_with_http_info(**kwargs)

    def credential_definitions_post(
        self,
        **kwargs
    ):
        """Sends a credential definition to the ledger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.credential_definitions_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            conn_id (str): Connection identifier. [optional]
            create_transaction_for_endorser (bool): Create Transaction For Endorser's signature. [optional]
            body (CredentialDefinitionSendRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TxnOrCredentialDefinitionSendResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.credential_definitions_post_endpoint.call_with_http_info(**kwargs)
