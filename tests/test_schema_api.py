# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.schema_get_result import SchemaGetResult  # noqa: F401
from openapi_server.models.schema_send_request import SchemaSendRequest  # noqa: F401
from openapi_server.models.schemas_created_result import SchemasCreatedResult  # noqa: F401
from openapi_server.models.txn_or_schema_send_result import TxnOrSchemaSendResult  # noqa: F401


def test_schemas_created_get(client: TestClient):
    """Test case for schemas_created_get

    Search for matching schema that agent originated
    """
    params = [("schema_id", 'schema_id_example'),     ("schema_issuer_did", 'schema_issuer_did_example'),     ("schema_name", 'schema_name_example'),     ("schema_version", 'schema_version_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/schemas/created",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_schemas_post(client: TestClient):
    """Test case for schemas_post

    Sends a schema to the ledger
    """
    body = openapi_server.SchemaSendRequest()
    params = [("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/schemas",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_schemas_schema_id_get(client: TestClient):
    """Test case for schemas_schema_id_get

    Gets a schema from the ledger
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/schemas/{schema_id}".format(schema_id='schema_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_schemas_schema_id_write_record_post(client: TestClient):
    """Test case for schemas_schema_id_write_record_post

    Writes a schema non-secret record to the wallet
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/schemas/{schema_id}/write_record".format(schema_id='schema_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

