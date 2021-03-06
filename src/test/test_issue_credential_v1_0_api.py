"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.7.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.issue_credential_v1_0_api import IssueCredentialV10Api  # noqa: E501


class TestIssueCredentialV10Api(unittest.TestCase):
    """IssueCredentialV10Api unit test stubs"""

    def setUp(self):
        self.api = IssueCredentialV10Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_issue_credential_create_offer_post(self):
        """Test case for issue_credential_create_offer_post

        Create a credential offer, independent of any proposal or connection  # noqa: E501
        """
        pass

    def test_issue_credential_create_post(self):
        """Test case for issue_credential_create_post

        Send holder a credential, automating entire flow  # noqa: E501
        """
        pass

    def test_issue_credential_records_cred_ex_id_delete(self):
        """Test case for issue_credential_records_cred_ex_id_delete

        Remove an existing credential exchange record  # noqa: E501
        """
        pass

    def test_issue_credential_records_cred_ex_id_get(self):
        """Test case for issue_credential_records_cred_ex_id_get

        Fetch a single credential exchange record  # noqa: E501
        """
        pass

    def test_issue_credential_records_cred_ex_id_issue_post(self):
        """Test case for issue_credential_records_cred_ex_id_issue_post

        Send holder a credential  # noqa: E501
        """
        pass

    def test_issue_credential_records_cred_ex_id_problem_report_post(self):
        """Test case for issue_credential_records_cred_ex_id_problem_report_post

        Send a problem report for credential exchange  # noqa: E501
        """
        pass

    def test_issue_credential_records_cred_ex_id_send_offer_post(self):
        """Test case for issue_credential_records_cred_ex_id_send_offer_post

        Send holder a credential offer in reference to a proposal with preview  # noqa: E501
        """
        pass

    def test_issue_credential_records_cred_ex_id_send_request_post(self):
        """Test case for issue_credential_records_cred_ex_id_send_request_post

        Send issuer a credential request  # noqa: E501
        """
        pass

    def test_issue_credential_records_cred_ex_id_store_post(self):
        """Test case for issue_credential_records_cred_ex_id_store_post

        Store a received credential  # noqa: E501
        """
        pass

    def test_issue_credential_records_get(self):
        """Test case for issue_credential_records_get

        Fetch all credential exchange records  # noqa: E501
        """
        pass

    def test_issue_credential_send_offer_post(self):
        """Test case for issue_credential_send_offer_post

        Send holder a credential offer, independent of any proposal  # noqa: E501
        """
        pass

    def test_issue_credential_send_post(self):
        """Test case for issue_credential_send_post

        Send holder a credential, automating entire flow  # noqa: E501
        """
        pass

    def test_issue_credential_send_proposal_post(self):
        """Test case for issue_credential_send_proposal_post

        Send issuer a credential proposal  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
