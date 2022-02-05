# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.get_did_endpoint_response import GetDIDEndpointResponse  # noqa: F401
from openapi_server.models.get_did_verkey_response import GetDIDVerkeyResponse  # noqa: F401
from openapi_server.models.get_nym_role_response import GetNymRoleResponse  # noqa: F401
from openapi_server.models.register_ledger_nym_response import RegisterLedgerNymResponse  # noqa: F401
from openapi_server.models.taa_accept import TAAAccept  # noqa: F401
from openapi_server.models.taa_result import TAAResult  # noqa: F401


def test_ledger_did_endpoint_get(client: TestClient):
    """Test case for ledger_did_endpoint_get

    Get the endpoint for a DID from the ledger.
    """
    params = [("did", 'did_example'),     ("endpoint_type", 'endpoint_type_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/ledger/did-endpoint",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_ledger_did_verkey_get(client: TestClient):
    """Test case for ledger_did_verkey_get

    Get the verkey for a DID from the ledger.
    """
    params = [("did", 'did_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/ledger/did-verkey",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_ledger_get_nym_role_get(client: TestClient):
    """Test case for ledger_get_nym_role_get

    Get the role from the NYM registration of a public DID.
    """
    params = [("did", 'did_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/ledger/get-nym-role",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_ledger_register_nym_post(client: TestClient):
    """Test case for ledger_register_nym_post

    Send a NYM registration to the ledger.
    """
    params = [("did", 'did_example'),     ("verkey", 'verkey_example'),     ("alias", 'alias_example'),     ("role", 'role_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/ledger/register-nym",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_ledger_rotate_public_did_keypair_patch(client: TestClient):
    """Test case for ledger_rotate_public_did_keypair_patch

    Rotate key pair for public DID.
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PATCH",
        "/ledger/rotate-public-did-keypair",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_ledger_taa_accept_post(client: TestClient):
    """Test case for ledger_taa_accept_post

    Accept the transaction author agreement
    """
    body = openapi_server.TAAAccept()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/ledger/taa/accept",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_ledger_taa_get(client: TestClient):
    """Test case for ledger_taa_get

    Fetch the current transaction author agreement, if any
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/ledger/taa",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

