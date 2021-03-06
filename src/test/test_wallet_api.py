"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.7.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.wallet_api import WalletApi  # noqa: E501


class TestWalletApi(unittest.TestCase):
    """WalletApi unit test stubs"""

    def setUp(self):
        self.api = WalletApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_wallet_did_create_post(self):
        """Test case for wallet_did_create_post

        Create a local DID  # noqa: E501
        """
        pass

    def test_wallet_did_get(self):
        """Test case for wallet_did_get

        List wallet DIDs  # noqa: E501
        """
        pass

    def test_wallet_did_local_rotate_keypair_patch(self):
        """Test case for wallet_did_local_rotate_keypair_patch

        Rotate keypair for a DID not posted to the ledger  # noqa: E501
        """
        pass

    def test_wallet_did_public_get(self):
        """Test case for wallet_did_public_get

        Fetch the current public DID  # noqa: E501
        """
        pass

    def test_wallet_did_public_post(self):
        """Test case for wallet_did_public_post

        Assign the current public DID  # noqa: E501
        """
        pass

    def test_wallet_get_did_endpoint_get(self):
        """Test case for wallet_get_did_endpoint_get

        Query DID endpoint in wallet  # noqa: E501
        """
        pass

    def test_wallet_set_did_endpoint_post(self):
        """Test case for wallet_set_did_endpoint_post

        Update endpoint in wallet and on ledger if posted to it  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
