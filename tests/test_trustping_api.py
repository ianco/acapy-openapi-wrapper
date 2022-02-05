# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.ping_request import PingRequest  # noqa: F401
from openapi_server.models.ping_request_response import PingRequestResponse  # noqa: F401


def test_connections_conn_id_send_ping_post(client: TestClient):
    """Test case for connections_conn_id_send_ping_post

    Send a trust ping to a connection
    """
    body = openapi_server.PingRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/send-ping".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

