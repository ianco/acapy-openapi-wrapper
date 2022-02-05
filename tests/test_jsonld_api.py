# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.sign_request import SignRequest  # noqa: F401
from openapi_server.models.sign_response import SignResponse  # noqa: F401
from openapi_server.models.verify_request import VerifyRequest  # noqa: F401
from openapi_server.models.verify_response import VerifyResponse  # noqa: F401


def test_jsonld_sign_post(client: TestClient):
    """Test case for jsonld_sign_post

    Sign a JSON-LD structure and return it
    """
    body = openapi_server.SignRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/jsonld/sign",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_jsonld_verify_post(client: TestClient):
    """Test case for jsonld_verify_post

    Verify a JSON-LD structure.
    """
    body = openapi_server.VerifyRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/jsonld/verify",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

