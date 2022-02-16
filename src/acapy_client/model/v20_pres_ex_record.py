"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.7.2
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from acapy_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from acapy_client.exceptions import ApiAttributeError


def lazy_import():
    from acapy_client.model.v20_pres import V20Pres
    from acapy_client.model.v20_pres_ex_record_by_format import V20PresExRecordByFormat
    from acapy_client.model.v20_pres_proposal import V20PresProposal
    from acapy_client.model.v20_pres_request import V20PresRequest
    globals()['V20Pres'] = V20Pres
    globals()['V20PresExRecordByFormat'] = V20PresExRecordByFormat
    globals()['V20PresProposal'] = V20PresProposal
    globals()['V20PresRequest'] = V20PresRequest


class V20PresExRecord(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('initiator',): {
            'SELF': "self",
            'EXTERNAL': "external",
        },
        ('role',): {
            'PROVER': "prover",
            'VERIFIER': "verifier",
        },
        ('state',): {
            'PROPOSAL-SENT': "proposal-sent",
            'PROPOSAL-RECEIVED': "proposal-received",
            'REQUEST-SENT': "request-sent",
            'REQUEST-RECEIVED': "request-received",
            'PRESENTATION-SENT': "presentation-sent",
            'PRESENTATION-RECEIVED': "presentation-received",
            'DONE': "done",
            'ABANDONED': "abandoned",
        },
        ('verified',): {
            'TRUE': "true",
            'FALSE': "false",
        },
    }

    validations = {
        ('created_at',): {
            'regex': {
                'pattern': r'^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$',  # noqa: E501
            },
        },
        ('updated_at',): {
            'regex': {
                'pattern': r'^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'auto_present': (bool,),  # noqa: E501
            'by_format': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'connection_id': (str,),  # noqa: E501
            'created_at': (str,),  # noqa: E501
            'error_msg': (str,),  # noqa: E501
            'initiator': (str,),  # noqa: E501
            'pres': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'pres_ex_id': (str,),  # noqa: E501
            'pres_proposal': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'pres_request': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'role': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'thread_id': (str,),  # noqa: E501
            'trace': (bool,),  # noqa: E501
            'updated_at': (str,),  # noqa: E501
            'verified': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'auto_present': 'auto_present',  # noqa: E501
        'by_format': 'by_format',  # noqa: E501
        'connection_id': 'connection_id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'error_msg': 'error_msg',  # noqa: E501
        'initiator': 'initiator',  # noqa: E501
        'pres': 'pres',  # noqa: E501
        'pres_ex_id': 'pres_ex_id',  # noqa: E501
        'pres_proposal': 'pres_proposal',  # noqa: E501
        'pres_request': 'pres_request',  # noqa: E501
        'role': 'role',  # noqa: E501
        'state': 'state',  # noqa: E501
        'thread_id': 'thread_id',  # noqa: E501
        'trace': 'trace',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'verified': 'verified',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """V20PresExRecord - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            auto_present (bool): Prover choice to auto-present proof as verifier requests. [optional]  # noqa: E501
            by_format ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Attachment content by format for proposal, request, and presentation. [optional]  # noqa: E501
            connection_id (str): Connection identifier. [optional]  # noqa: E501
            created_at (str): Time of record creation. [optional]  # noqa: E501
            error_msg (str): Error message. [optional]  # noqa: E501
            initiator (str): Present-proof exchange initiator: self or external. [optional]  # noqa: E501
            pres ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Presentation message. [optional]  # noqa: E501
            pres_ex_id (str): Presentation exchange identifier. [optional]  # noqa: E501
            pres_proposal ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Presentation proposal message. [optional]  # noqa: E501
            pres_request ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Presentation request message. [optional]  # noqa: E501
            role (str): Present-proof exchange role: prover or verifier. [optional]  # noqa: E501
            state (str): Present-proof exchange state. [optional]  # noqa: E501
            thread_id (str): Thread identifier. [optional]  # noqa: E501
            trace (bool): Record trace information, based on agent configuration. [optional]  # noqa: E501
            updated_at (str): Time of last record update. [optional]  # noqa: E501
            verified (str): Whether presentation is verified: 'true' or 'false'. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """V20PresExRecord - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            auto_present (bool): Prover choice to auto-present proof as verifier requests. [optional]  # noqa: E501
            by_format ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Attachment content by format for proposal, request, and presentation. [optional]  # noqa: E501
            connection_id (str): Connection identifier. [optional]  # noqa: E501
            created_at (str): Time of record creation. [optional]  # noqa: E501
            error_msg (str): Error message. [optional]  # noqa: E501
            initiator (str): Present-proof exchange initiator: self or external. [optional]  # noqa: E501
            pres ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Presentation message. [optional]  # noqa: E501
            pres_ex_id (str): Presentation exchange identifier. [optional]  # noqa: E501
            pres_proposal ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Presentation proposal message. [optional]  # noqa: E501
            pres_request ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Presentation request message. [optional]  # noqa: E501
            role (str): Present-proof exchange role: prover or verifier. [optional]  # noqa: E501
            state (str): Present-proof exchange state. [optional]  # noqa: E501
            thread_id (str): Thread identifier. [optional]  # noqa: E501
            trace (bool): Record trace information, based on agent configuration. [optional]  # noqa: E501
            updated_at (str): Time of last record update. [optional]  # noqa: E501
            verified (str): Whether presentation is verified: 'true' or 'false'. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
