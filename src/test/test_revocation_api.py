"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.7.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.revocation_api import RevocationApi  # noqa: E501


class TestRevocationApi(unittest.TestCase):
    """RevocationApi unit test stubs"""

    def setUp(self):
        self.api = RevocationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_revocation_active_registry_cred_def_id_get(self):
        """Test case for revocation_active_registry_cred_def_id_get

        Get current active revocation registry by credential definition id  # noqa: E501
        """
        pass

    def test_revocation_clear_pending_revocations_post(self):
        """Test case for revocation_clear_pending_revocations_post

        Clear pending revocations  # noqa: E501
        """
        pass

    def test_revocation_create_registry_post(self):
        """Test case for revocation_create_registry_post

        Creates a new revocation registry  # noqa: E501
        """
        pass

    def test_revocation_credential_record_get(self):
        """Test case for revocation_credential_record_get

        Get credential revocation status  # noqa: E501
        """
        pass

    def test_revocation_publish_revocations_post(self):
        """Test case for revocation_publish_revocations_post

        Publish pending revocations to ledger  # noqa: E501
        """
        pass

    def test_revocation_registries_created_get(self):
        """Test case for revocation_registries_created_get

        Search for matching revocation registries that current agent created  # noqa: E501
        """
        pass

    def test_revocation_registry_rev_reg_id_definition_post(self):
        """Test case for revocation_registry_rev_reg_id_definition_post

        Send revocation registry definition to ledger  # noqa: E501
        """
        pass

    def test_revocation_registry_rev_reg_id_entry_post(self):
        """Test case for revocation_registry_rev_reg_id_entry_post

        Send revocation registry entry to ledger  # noqa: E501
        """
        pass

    def test_revocation_registry_rev_reg_id_get(self):
        """Test case for revocation_registry_rev_reg_id_get

        Get revocation registry by revocation registry id  # noqa: E501
        """
        pass

    def test_revocation_registry_rev_reg_id_issued_get(self):
        """Test case for revocation_registry_rev_reg_id_issued_get

        Get number of credentials issued against revocation registry  # noqa: E501
        """
        pass

    def test_revocation_registry_rev_reg_id_patch(self):
        """Test case for revocation_registry_rev_reg_id_patch

        Update revocation registry with new public URI to its tails file  # noqa: E501
        """
        pass

    def test_revocation_registry_rev_reg_id_set_state_patch(self):
        """Test case for revocation_registry_rev_reg_id_set_state_patch

        Set revocation registry state manually  # noqa: E501
        """
        pass

    def test_revocation_registry_rev_reg_id_tails_file_get(self):
        """Test case for revocation_registry_rev_reg_id_tails_file_get

        Download tails file  # noqa: E501
        """
        pass

    def test_revocation_registry_rev_reg_id_tails_file_put(self):
        """Test case for revocation_registry_rev_reg_id_tails_file_put

        Upload local tails file to server  # noqa: E501
        """
        pass

    def test_revocation_revoke_post(self):
        """Test case for revocation_revoke_post

        Revoke an issued credential  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()