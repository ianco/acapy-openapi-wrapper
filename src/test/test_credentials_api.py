"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.7.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.credentials_api import CredentialsApi  # noqa: E501


class TestCredentialsApi(unittest.TestCase):
    """CredentialsApi unit test stubs"""

    def setUp(self):
        self.api = CredentialsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_credential_credential_id_delete(self):
        """Test case for credential_credential_id_delete

        Remove credential from wallet by id  # noqa: E501
        """
        pass

    def test_credential_credential_id_get(self):
        """Test case for credential_credential_id_get

        Fetch credential from wallet by id  # noqa: E501
        """
        pass

    def test_credential_mime_types_credential_id_get(self):
        """Test case for credential_mime_types_credential_id_get

        Get attribute MIME types from wallet  # noqa: E501
        """
        pass

    def test_credential_revoked_credential_id_get(self):
        """Test case for credential_revoked_credential_id_get

        Query credential revocation status by id  # noqa: E501
        """
        pass

    def test_credential_w3c_credential_id_delete(self):
        """Test case for credential_w3c_credential_id_delete

        Remove W3C credential from wallet by id  # noqa: E501
        """
        pass

    def test_credential_w3c_credential_id_get(self):
        """Test case for credential_w3c_credential_id_get

        Fetch W3C credential from wallet by id  # noqa: E501
        """
        pass

    def test_credentials_get(self):
        """Test case for credentials_get

        Fetch credentials from wallet  # noqa: E501
        """
        pass

    def test_credentials_w3c_post(self):
        """Test case for credentials_w3c_post

        Fetch W3C credentials from wallet  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
