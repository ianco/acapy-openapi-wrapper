# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.did_create import DIDCreate  # noqa: F401
from openapi_server.models.did_endpoint import DIDEndpoint  # noqa: F401
from openapi_server.models.did_endpoint_with_type import DIDEndpointWithType  # noqa: F401
from openapi_server.models.did_list import DIDList  # noqa: F401
from openapi_server.models.did_result import DIDResult  # noqa: F401


def test_wallet_did_create_post(client: TestClient):
    """Test case for wallet_did_create_post

    Create a local DID
    """
    body = openapi_server.DIDCreate()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/wallet/did/create",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wallet_did_get(client: TestClient):
    """Test case for wallet_did_get

    List wallet DIDs
    """
    params = [("did", 'did_example'),     ("key_type", 'key_type_example'),     ("method", 'method_example'),     ("posture", 'posture_example'),     ("verkey", 'verkey_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/wallet/did",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wallet_did_local_rotate_keypair_patch(client: TestClient):
    """Test case for wallet_did_local_rotate_keypair_patch

    Rotate keypair for a DID not posted to the ledger
    """
    params = [("did", 'did_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PATCH",
        "/wallet/did/local/rotate-keypair",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wallet_did_public_get(client: TestClient):
    """Test case for wallet_did_public_get

    Fetch the current public DID
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/wallet/did/public",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wallet_did_public_post(client: TestClient):
    """Test case for wallet_did_public_post

    Assign the current public DID
    """
    params = [("did", 'did_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/wallet/did/public",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wallet_get_did_endpoint_get(client: TestClient):
    """Test case for wallet_get_did_endpoint_get

    Query DID endpoint in wallet
    """
    params = [("did", 'did_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/wallet/get-did-endpoint",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wallet_set_did_endpoint_post(client: TestClient):
    """Test case for wallet_set_did_endpoint_post

    Update endpoint in wallet and on ledger if posted to it
    """
    body = openapi_server.DIDEndpointWithType()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/wallet/set-did-endpoint",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

