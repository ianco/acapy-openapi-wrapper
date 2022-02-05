# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.create_wallet_request import CreateWalletRequest  # noqa: F401
from openapi_server.models.create_wallet_response import CreateWalletResponse  # noqa: F401
from openapi_server.models.create_wallet_token_request import CreateWalletTokenRequest  # noqa: F401
from openapi_server.models.create_wallet_token_response import CreateWalletTokenResponse  # noqa: F401
from openapi_server.models.remove_wallet_request import RemoveWalletRequest  # noqa: F401
from openapi_server.models.update_wallet_request import UpdateWalletRequest  # noqa: F401
from openapi_server.models.wallet_list import WalletList  # noqa: F401
from openapi_server.models.wallet_record import WalletRecord  # noqa: F401


def test_multitenancy_wallet_post(client: TestClient):
    """Test case for multitenancy_wallet_post

    Create a subwallet
    """
    body = openapi_server.CreateWalletRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/multitenancy/wallet",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_multitenancy_wallet_wallet_id_get(client: TestClient):
    """Test case for multitenancy_wallet_wallet_id_get

    Get a single subwallet
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/multitenancy/wallet/{wallet_id}".format(wallet_id='wallet_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_multitenancy_wallet_wallet_id_put(client: TestClient):
    """Test case for multitenancy_wallet_wallet_id_put

    Update a subwallet
    """
    body = openapi_server.UpdateWalletRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PUT",
        "/multitenancy/wallet/{wallet_id}".format(wallet_id='wallet_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_multitenancy_wallet_wallet_id_remove_post(client: TestClient):
    """Test case for multitenancy_wallet_wallet_id_remove_post

    Remove a subwallet
    """
    body = openapi_server.RemoveWalletRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/multitenancy/wallet/{wallet_id}/remove".format(wallet_id='wallet_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_multitenancy_wallet_wallet_id_token_post(client: TestClient):
    """Test case for multitenancy_wallet_wallet_id_token_post

    Get auth token for a subwallet
    """
    body = openapi_server.CreateWalletTokenRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/multitenancy/wallet/{wallet_id}/token".format(wallet_id='wallet_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_multitenancy_wallets_get(client: TestClient):
    """Test case for multitenancy_wallets_get

    Query subwallets
    """
    params = [("wallet_name", 'wallet_name_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/multitenancy/wallets",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

