# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.admin_mediation_deny import AdminMediationDeny  # noqa: F401
from openapi_server.models.keylist import Keylist  # noqa: F401
from openapi_server.models.keylist_query import KeylistQuery  # noqa: F401
from openapi_server.models.keylist_query_filter_request import KeylistQueryFilterRequest  # noqa: F401
from openapi_server.models.keylist_update import KeylistUpdate  # noqa: F401
from openapi_server.models.keylist_update_request import KeylistUpdateRequest  # noqa: F401
from openapi_server.models.mediation_create_request import MediationCreateRequest  # noqa: F401
from openapi_server.models.mediation_deny import MediationDeny  # noqa: F401
from openapi_server.models.mediation_grant import MediationGrant  # noqa: F401
from openapi_server.models.mediation_list import MediationList  # noqa: F401
from openapi_server.models.mediation_record import MediationRecord  # noqa: F401


def test_mediation_default_mediator_delete(client: TestClient):
    """Test case for mediation_default_mediator_delete

    Clear default mediator
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/mediation/default-mediator",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_default_mediator_get(client: TestClient):
    """Test case for mediation_default_mediator_get

    Get default mediator
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/mediation/default-mediator",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_keylists_get(client: TestClient):
    """Test case for mediation_keylists_get

    Retrieve keylists by connection or role
    """
    params = [("conn_id", 'conn_id_example'),     ("role", 'server')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/mediation/keylists",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_keylists_mediation_id_send_keylist_query_post(client: TestClient):
    """Test case for mediation_keylists_mediation_id_send_keylist_query_post

    Send keylist query to mediator
    """
    body = openapi_server.KeylistQueryFilterRequest()
    params = [("paginate_limit", -1),     ("paginate_offset", 0)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/keylists/{mediation_id}/send-keylist-query".format(mediation_id='mediation_id_example'),
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_keylists_mediation_id_send_keylist_update_post(client: TestClient):
    """Test case for mediation_keylists_mediation_id_send_keylist_update_post

    Send keylist update to mediator
    """
    body = openapi_server.KeylistUpdateRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/keylists/{mediation_id}/send-keylist-update".format(mediation_id='mediation_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_mediation_id_default_mediator_put(client: TestClient):
    """Test case for mediation_mediation_id_default_mediator_put

    Set default mediator
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PUT",
        "/mediation/{mediation_id}/default-mediator".format(mediation_id='mediation_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_request_conn_id_post(client: TestClient):
    """Test case for mediation_request_conn_id_post

    Request mediation from connection
    """
    body = openapi_server.MediationCreateRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/request/{conn_id}".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_requests_get(client: TestClient):
    """Test case for mediation_requests_get

    Query mediation requests, returns list of all mediation records
    """
    params = [("conn_id", 'conn_id_example'),     ("mediator_terms", ['mediator_terms_example']),     ("recipient_terms", ['recipient_terms_example']),     ("state", 'state_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/mediation/requests",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_requests_mediation_id_delete(client: TestClient):
    """Test case for mediation_requests_mediation_id_delete

    Delete mediation request by ID
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/mediation/requests/{mediation_id}".format(mediation_id='mediation_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_requests_mediation_id_deny_post(client: TestClient):
    """Test case for mediation_requests_mediation_id_deny_post

    Deny a stored mediation request
    """
    body = openapi_server.AdminMediationDeny()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/requests/{mediation_id}/deny".format(mediation_id='mediation_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_requests_mediation_id_get(client: TestClient):
    """Test case for mediation_requests_mediation_id_get

    Retrieve mediation request record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/mediation/requests/{mediation_id}".format(mediation_id='mediation_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mediation_requests_mediation_id_grant_post(client: TestClient):
    """Test case for mediation_requests_mediation_id_grant_post

    Grant received mediation
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/requests/{mediation_id}/grant".format(mediation_id='mediation_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

