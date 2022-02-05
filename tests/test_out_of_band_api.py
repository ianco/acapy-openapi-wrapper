# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.conn_record import ConnRecord  # noqa: F401
from openapi_server.models.invitation_create_request import InvitationCreateRequest  # noqa: F401
from openapi_server.models.invitation_message import InvitationMessage  # noqa: F401
from openapi_server.models.invitation_record import InvitationRecord  # noqa: F401


def test_out_of_band_create_invitation_post(client: TestClient):
    """Test case for out_of_band_create_invitation_post

    Create a new connection invitation
    """
    body = openapi_server.InvitationCreateRequest()
    params = [("auto_accept", True),     ("multi_use", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/out-of-band/create-invitation",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_out_of_band_receive_invitation_post(client: TestClient):
    """Test case for out_of_band_receive_invitation_post

    Receive a new connection invitation
    """
    body = openapi_server.InvitationMessage()
    params = [("alias", 'alias_example'),     ("auto_accept", True),     ("mediation_id", 'mediation_id_example'),     ("use_existing_connection", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/out-of-band/receive-invitation",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

