# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.admin_config import AdminConfig  # noqa: F401
from openapi_server.models.admin_modules import AdminModules  # noqa: F401
from openapi_server.models.admin_status import AdminStatus  # noqa: F401
from openapi_server.models.admin_status_liveliness import AdminStatusLiveliness  # noqa: F401
from openapi_server.models.admin_status_readiness import AdminStatusReadiness  # noqa: F401
from openapi_server.models.query_result import QueryResult  # noqa: F401


def test_features_get(client: TestClient):
    """Test case for features_get

    Query supported features
    """
    params = [("query", 'query_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/features",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_plugins_get(client: TestClient):
    """Test case for plugins_get

    Fetch the list of loaded plugins
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/plugins",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_shutdown_get(client: TestClient):
    """Test case for shutdown_get

    Shut down server
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/shutdown",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_status_config_get(client: TestClient):
    """Test case for status_config_get

    Fetch the server configuration
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/status/config",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_status_get(client: TestClient):
    """Test case for status_get

    Fetch the server status
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/status",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_status_live_get(client: TestClient):
    """Test case for status_live_get

    Liveliness check
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/status/live",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_status_ready_get(client: TestClient):
    """Test case for status_ready_get

    Readiness check
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/status/ready",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_status_reset_post(client: TestClient):
    """Test case for status_reset_post

    Reset statistics
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/status/reset",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

