# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.action_menu_fetch_result import ActionMenuFetchResult  # noqa: F401
from openapi_server.models.perform_request import PerformRequest  # noqa: F401
from openapi_server.models.send_menu import SendMenu  # noqa: F401


def test_action_menu_conn_id_close_post(client: TestClient):
    """Test case for action_menu_conn_id_close_post

    Close the active menu associated with a connection
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/action-menu/{conn_id}/close".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_action_menu_conn_id_fetch_post(client: TestClient):
    """Test case for action_menu_conn_id_fetch_post

    Fetch the active menu
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/action-menu/{conn_id}/fetch".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_action_menu_conn_id_perform_post(client: TestClient):
    """Test case for action_menu_conn_id_perform_post

    Perform an action associated with the active menu
    """
    body = openapi_server.PerformRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/action-menu/{conn_id}/perform".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_action_menu_conn_id_request_post(client: TestClient):
    """Test case for action_menu_conn_id_request_post

    Request the active menu
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/action-menu/{conn_id}/request".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_action_menu_conn_id_send_menu_post(client: TestClient):
    """Test case for action_menu_conn_id_send_menu_post

    Send an action menu to a connection
    """
    body = openapi_server.SendMenu()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/action-menu/{conn_id}/send-menu".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

