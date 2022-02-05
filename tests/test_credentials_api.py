# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.attribute_mime_types_result import AttributeMimeTypesResult  # noqa: F401
from openapi_server.models.cred_info_list import CredInfoList  # noqa: F401
from openapi_server.models.cred_revoked_result import CredRevokedResult  # noqa: F401
from openapi_server.models.indy_cred_info import IndyCredInfo  # noqa: F401
from openapi_server.models.vc_record import VCRecord  # noqa: F401
from openapi_server.models.vc_record_list import VCRecordList  # noqa: F401
from openapi_server.models.w3_c_credentials_list_request import W3CCredentialsListRequest  # noqa: F401


def test_credential_credential_id_delete(client: TestClient):
    """Test case for credential_credential_id_delete

    Remove credential from wallet by id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/credential/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credential_credential_id_get(client: TestClient):
    """Test case for credential_credential_id_get

    Fetch credential from wallet by id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credential_mime_types_credential_id_get(client: TestClient):
    """Test case for credential_mime_types_credential_id_get

    Get attribute MIME types from wallet
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential/mime-types/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credential_revoked_credential_id_get(client: TestClient):
    """Test case for credential_revoked_credential_id_get

    Query credential revocation status by id
    """
    params = [("_from", '_from_example'),     ("to", 'to_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential/revoked/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credential_w3c_credential_id_delete(client: TestClient):
    """Test case for credential_w3c_credential_id_delete

    Remove W3C credential from wallet by id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/credential/w3c/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credential_w3c_credential_id_get(client: TestClient):
    """Test case for credential_w3c_credential_id_get

    Fetch W3C credential from wallet by id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential/w3c/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credentials_get(client: TestClient):
    """Test case for credentials_get

    Fetch credentials from wallet
    """
    params = [("count", 'count_example'),     ("start", 'start_example'),     ("wql", 'wql_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credentials",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credentials_w3c_post(client: TestClient):
    """Test case for credentials_w3c_post

    Fetch W3C credentials from wallet
    """
    body = openapi_server.W3CCredentialsListRequest()
    params = [("count", 'count_example'),     ("start", 'start_example'),     ("wql", 'wql_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/credentials/w3c",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

