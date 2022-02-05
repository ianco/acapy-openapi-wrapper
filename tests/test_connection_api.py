# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.conn_record import ConnRecord  # noqa: F401
from openapi_server.models.connection_list import ConnectionList  # noqa: F401
from openapi_server.models.connection_metadata import ConnectionMetadata  # noqa: F401
from openapi_server.models.connection_metadata_set_request import ConnectionMetadataSetRequest  # noqa: F401
from openapi_server.models.connection_static_request import ConnectionStaticRequest  # noqa: F401
from openapi_server.models.connection_static_result import ConnectionStaticResult  # noqa: F401
from openapi_server.models.create_invitation_request import CreateInvitationRequest  # noqa: F401
from openapi_server.models.endpoints_result import EndpointsResult  # noqa: F401
from openapi_server.models.invitation_result import InvitationResult  # noqa: F401
from openapi_server.models.receive_invitation_request import ReceiveInvitationRequest  # noqa: F401


def test_connections_conn_id_accept_invitation_post(client: TestClient):
    """Test case for connections_conn_id_accept_invitation_post

    Accept a stored connection invitation
    """
    params = [("mediation_id", 'mediation_id_example'),     ("my_endpoint", 'my_endpoint_example'),     ("my_label", 'my_label_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/accept-invitation".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_conn_id_accept_request_post(client: TestClient):
    """Test case for connections_conn_id_accept_request_post

    Accept a stored connection request
    """
    params = [("my_endpoint", 'my_endpoint_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/accept-request".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_conn_id_delete(client: TestClient):
    """Test case for connections_conn_id_delete

    Remove an existing connection record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/connections/{conn_id}".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_conn_id_endpoints_get(client: TestClient):
    """Test case for connections_conn_id_endpoints_get

    Fetch connection remote endpoint
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/connections/{conn_id}/endpoints".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_conn_id_establish_inbound_ref_id_post(client: TestClient):
    """Test case for connections_conn_id_establish_inbound_ref_id_post

    Assign another connection as the inbound connection
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/establish-inbound/{ref_id}".format(conn_id='conn_id_example', ref_id='ref_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_conn_id_get(client: TestClient):
    """Test case for connections_conn_id_get

    Fetch a single connection record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/connections/{conn_id}".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_conn_id_metadata_get(client: TestClient):
    """Test case for connections_conn_id_metadata_get

    Fetch connection metadata
    """
    params = [("key", 'key_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/connections/{conn_id}/metadata".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_conn_id_metadata_post(client: TestClient):
    """Test case for connections_conn_id_metadata_post

    Set connection metadata
    """
    body = openapi_server.ConnectionMetadataSetRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/metadata".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_create_invitation_post(client: TestClient):
    """Test case for connections_create_invitation_post

    Create a new connection invitation
    """
    body = openapi_server.CreateInvitationRequest()
    params = [("alias", 'alias_example'),     ("auto_accept", True),     ("multi_use", True),     ("public", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/create-invitation",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_create_static_post(client: TestClient):
    """Test case for connections_create_static_post

    Create a new static connection
    """
    body = openapi_server.ConnectionStaticRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/create-static",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_get(client: TestClient):
    """Test case for connections_get

    Query agent-to-agent connections
    """
    params = [("alias", 'alias_example'),     ("connection_protocol", 'connection_protocol_example'),     ("invitation_key", 'invitation_key_example'),     ("my_did", 'my_did_example'),     ("state", 'state_example'),     ("their_did", 'their_did_example'),     ("their_role", 'their_role_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/connections",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_connections_receive_invitation_post(client: TestClient):
    """Test case for connections_receive_invitation_post

    Receive a new connection invitation
    """
    body = openapi_server.ReceiveInvitationRequest()
    params = [("alias", 'alias_example'),     ("auto_accept", True),     ("mediation_id", 'mediation_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/receive-invitation",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

