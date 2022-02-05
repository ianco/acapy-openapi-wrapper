# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.conn_record import ConnRecord  # noqa: F401
from openapi_server.models.didx_request import DIDXRequest  # noqa: F401


def test_didexchange_conn_id_accept_invitation_post(client: TestClient):
    """Test case for didexchange_conn_id_accept_invitation_post

    Accept a stored connection invitation
    """
    params = [("my_endpoint", 'my_endpoint_example'),     ("my_label", 'my_label_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/didexchange/{conn_id}/accept-invitation".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_didexchange_conn_id_accept_request_post(client: TestClient):
    """Test case for didexchange_conn_id_accept_request_post

    Accept a stored connection request
    """
    params = [("mediation_id", 'mediation_id_example'),     ("my_endpoint", 'my_endpoint_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/didexchange/{conn_id}/accept-request".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_didexchange_create_request_post(client: TestClient):
    """Test case for didexchange_create_request_post

    Create and send a request against public DID's implicit invitation
    """
    params = [("their_public_did", 'their_public_did_example'),     ("mediation_id", 'mediation_id_example'),     ("my_endpoint", 'my_endpoint_example'),     ("my_label", 'my_label_example'),     ("use_public_did", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/didexchange/create-request",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_didexchange_receive_request_post(client: TestClient):
    """Test case for didexchange_receive_request_post

    Receive request against public DID's implicit invitation
    """
    body = openapi_server.DIDXRequest()
    params = [("alias", 'alias_example'),     ("auto_accept", True),     ("mediation_id", 'mediation_id_example'),     ("my_endpoint", 'my_endpoint_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/didexchange/receive-request",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

