# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.credential_definition_get_result import CredentialDefinitionGetResult  # noqa: F401
from openapi_server.models.credential_definition_send_request import CredentialDefinitionSendRequest  # noqa: F401
from openapi_server.models.credential_definitions_created_result import CredentialDefinitionsCreatedResult  # noqa: F401
from openapi_server.models.txn_or_credential_definition_send_result import TxnOrCredentialDefinitionSendResult  # noqa: F401


def test_credential_definitions_created_get(client: TestClient):
    """Test case for credential_definitions_created_get

    Search for matching credential definitions that agent originated
    """
    params = [("cred_def_id", 'cred_def_id_example'),     ("issuer_did", 'issuer_did_example'),     ("schema_id", 'schema_id_example'),     ("schema_issuer_did", 'schema_issuer_did_example'),     ("schema_name", 'schema_name_example'),     ("schema_version", 'schema_version_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential-definitions/created",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credential_definitions_cred_def_id_get(client: TestClient):
    """Test case for credential_definitions_cred_def_id_get

    Gets a credential definition from the ledger
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential-definitions/{cred_def_id}".format(cred_def_id='cred_def_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credential_definitions_cred_def_id_write_record_post(client: TestClient):
    """Test case for credential_definitions_cred_def_id_write_record_post

    Writes a credential definition non-secret record to the wallet
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/credential-definitions/{cred_def_id}/write_record".format(cred_def_id='cred_def_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credential_definitions_post(client: TestClient):
    """Test case for credential_definitions_post

    Sends a credential definition to the ledger
    """
    body = openapi_server.CredentialDefinitionSendRequest()
    params = [("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/credential-definitions",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

