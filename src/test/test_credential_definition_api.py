"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.7.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.credential_definition_api import CredentialDefinitionApi  # noqa: E501


class TestCredentialDefinitionApi(unittest.TestCase):
    """CredentialDefinitionApi unit test stubs"""

    def setUp(self):
        self.api = CredentialDefinitionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_credential_definitions_created_get(self):
        """Test case for credential_definitions_created_get

        Search for matching credential definitions that agent originated  # noqa: E501
        """
        pass

    def test_credential_definitions_cred_def_id_get(self):
        """Test case for credential_definitions_cred_def_id_get

        Gets a credential definition from the ledger  # noqa: E501
        """
        pass

    def test_credential_definitions_cred_def_id_write_record_post(self):
        """Test case for credential_definitions_cred_def_id_write_record_post

        Writes a credential definition non-secret record to the wallet  # noqa: E501
        """
        pass

    def test_credential_definitions_post(self):
        """Test case for credential_definitions_post

        Sends a credential definition to the ledger  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
