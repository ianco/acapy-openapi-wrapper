# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.send_message import SendMessage  # noqa: F401


def test_connections_conn_id_send_message_post(client: TestClient):
    """Test case for connections_conn_id_send_message_post

    Send a basic message to a connection
    """
    body = openapi_server.SendMessage()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/send-message".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

