"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.7.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.action_menu_api import ActionMenuApi  # noqa: E501


class TestActionMenuApi(unittest.TestCase):
    """ActionMenuApi unit test stubs"""

    def setUp(self):
        self.api = ActionMenuApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_action_menu_conn_id_close_post(self):
        """Test case for action_menu_conn_id_close_post

        Close the active menu associated with a connection  # noqa: E501
        """
        pass

    def test_action_menu_conn_id_fetch_post(self):
        """Test case for action_menu_conn_id_fetch_post

        Fetch the active menu  # noqa: E501
        """
        pass

    def test_action_menu_conn_id_perform_post(self):
        """Test case for action_menu_conn_id_perform_post

        Perform an action associated with the active menu  # noqa: E501
        """
        pass

    def test_action_menu_conn_id_request_post(self):
        """Test case for action_menu_conn_id_request_post

        Request the active menu  # noqa: E501
        """
        pass

    def test_action_menu_conn_id_send_menu_post(self):
        """Test case for action_menu_conn_id_send_menu_post

        Send an action menu to a connection  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
