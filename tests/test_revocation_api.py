# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.clear_pending_revocations_request import ClearPendingRevocationsRequest  # noqa: F401
from openapi_server.models.cred_rev_record_result import CredRevRecordResult  # noqa: F401
from openapi_server.models.publish_revocations import PublishRevocations  # noqa: F401
from openapi_server.models.rev_reg_create_request import RevRegCreateRequest  # noqa: F401
from openapi_server.models.rev_reg_issued_result import RevRegIssuedResult  # noqa: F401
from openapi_server.models.rev_reg_result import RevRegResult  # noqa: F401
from openapi_server.models.rev_reg_update_tails_file_uri import RevRegUpdateTailsFileUri  # noqa: F401
from openapi_server.models.rev_regs_created import RevRegsCreated  # noqa: F401
from openapi_server.models.revoke_request import RevokeRequest  # noqa: F401
from openapi_server.models.txn_or_publish_revocations_result import TxnOrPublishRevocationsResult  # noqa: F401
from openapi_server.models.txn_or_rev_reg_result import TxnOrRevRegResult  # noqa: F401


def test_revocation_active_registry_cred_def_id_get(client: TestClient):
    """Test case for revocation_active_registry_cred_def_id_get

    Get current active revocation registry by credential definition id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/active-registry/{cred_def_id}".format(cred_def_id='cred_def_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_clear_pending_revocations_post(client: TestClient):
    """Test case for revocation_clear_pending_revocations_post

    Clear pending revocations
    """
    body = openapi_server.ClearPendingRevocationsRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/clear-pending-revocations",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_create_registry_post(client: TestClient):
    """Test case for revocation_create_registry_post

    Creates a new revocation registry
    """
    body = openapi_server.RevRegCreateRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/create-registry",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_credential_record_get(client: TestClient):
    """Test case for revocation_credential_record_get

    Get credential revocation status
    """
    params = [("cred_ex_id", 'cred_ex_id_example'),     ("cred_rev_id", 'cred_rev_id_example'),     ("rev_reg_id", 'rev_reg_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/credential-record",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_publish_revocations_post(client: TestClient):
    """Test case for revocation_publish_revocations_post

    Publish pending revocations to ledger
    """
    body = openapi_server.PublishRevocations()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/publish-revocations",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_registries_created_get(client: TestClient):
    """Test case for revocation_registries_created_get

    Search for matching revocation registries that current agent created
    """
    params = [("cred_def_id", 'cred_def_id_example'),     ("state", 'state_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/registries/created",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_registry_rev_reg_id_definition_post(client: TestClient):
    """Test case for revocation_registry_rev_reg_id_definition_post

    Send revocation registry definition to ledger
    """
    params = [("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/registry/{rev_reg_id}/definition".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_registry_rev_reg_id_entry_post(client: TestClient):
    """Test case for revocation_registry_rev_reg_id_entry_post

    Send revocation registry entry to ledger
    """
    params = [("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/registry/{rev_reg_id}/entry".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_registry_rev_reg_id_get(client: TestClient):
    """Test case for revocation_registry_rev_reg_id_get

    Get revocation registry by revocation registry id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/registry/{rev_reg_id}".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_registry_rev_reg_id_issued_get(client: TestClient):
    """Test case for revocation_registry_rev_reg_id_issued_get

    Get number of credentials issued against revocation registry
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/registry/{rev_reg_id}/issued".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_registry_rev_reg_id_patch(client: TestClient):
    """Test case for revocation_registry_rev_reg_id_patch

    Update revocation registry with new public URI to its tails file
    """
    body = openapi_server.RevRegUpdateTailsFileUri()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PATCH",
        "/revocation/registry/{rev_reg_id}".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_registry_rev_reg_id_set_state_patch(client: TestClient):
    """Test case for revocation_registry_rev_reg_id_set_state_patch

    Set revocation registry state manually
    """
    params = [("state", 'state_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PATCH",
        "/revocation/registry/{rev_reg_id}/set-state".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_registry_rev_reg_id_tails_file_get(client: TestClient):
    """Test case for revocation_registry_rev_reg_id_tails_file_get

    Download tails file
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/registry/{rev_reg_id}/tails-file".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_registry_rev_reg_id_tails_file_put(client: TestClient):
    """Test case for revocation_registry_rev_reg_id_tails_file_put

    Upload local tails file to server
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PUT",
        "/revocation/registry/{rev_reg_id}/tails-file".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revocation_revoke_post(client: TestClient):
    """Test case for revocation_revoke_post

    Revoke an issued credential
    """
    body = openapi_server.RevokeRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/revoke",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

