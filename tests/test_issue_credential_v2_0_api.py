# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.v20_cred_bound_offer_request import V20CredBoundOfferRequest  # noqa: F401
from openapi_server.models.v20_cred_ex_free import V20CredExFree  # noqa: F401
from openapi_server.models.v20_cred_ex_record import V20CredExRecord  # noqa: F401
from openapi_server.models.v20_cred_ex_record_detail import V20CredExRecordDetail  # noqa: F401
from openapi_server.models.v20_cred_ex_record_list_result import V20CredExRecordListResult  # noqa: F401
from openapi_server.models.v20_cred_issue_problem_report_request import V20CredIssueProblemReportRequest  # noqa: F401
from openapi_server.models.v20_cred_issue_request import V20CredIssueRequest  # noqa: F401
from openapi_server.models.v20_cred_offer_conn_free_request import V20CredOfferConnFreeRequest  # noqa: F401
from openapi_server.models.v20_cred_offer_request import V20CredOfferRequest  # noqa: F401
from openapi_server.models.v20_cred_request_free import V20CredRequestFree  # noqa: F401
from openapi_server.models.v20_cred_request_request import V20CredRequestRequest  # noqa: F401
from openapi_server.models.v20_cred_store_request import V20CredStoreRequest  # noqa: F401
from openapi_server.models.v20_issue_cred_schema_core import V20IssueCredSchemaCore  # noqa: F401


def test_issue_credential20_create_offer_post(client: TestClient):
    """Test case for issue_credential20_create_offer_post

    Create a credential offer, independent of any proposal or connection
    """
    body = openapi_server.V20CredOfferConnFreeRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/create-offer",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_create_post(client: TestClient):
    """Test case for issue_credential20_create_post

    Create credential from attribute values
    """
    body = openapi_server.V20IssueCredSchemaCore()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/create",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_records_cred_ex_id_delete(client: TestClient):
    """Test case for issue_credential20_records_cred_ex_id_delete

    Remove an existing credential exchange record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/issue-credential-2.0/records/{cred_ex_id}".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_records_cred_ex_id_get(client: TestClient):
    """Test case for issue_credential20_records_cred_ex_id_get

    Fetch a single credential exchange record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/issue-credential-2.0/records/{cred_ex_id}".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_records_cred_ex_id_issue_post(client: TestClient):
    """Test case for issue_credential20_records_cred_ex_id_issue_post

    Send holder a credential
    """
    body = openapi_server.V20CredIssueRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/records/{cred_ex_id}/issue".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_records_cred_ex_id_problem_report_post(client: TestClient):
    """Test case for issue_credential20_records_cred_ex_id_problem_report_post

    Send a problem report for credential exchange
    """
    body = openapi_server.V20CredIssueProblemReportRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/records/{cred_ex_id}/problem-report".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_records_cred_ex_id_send_offer_post(client: TestClient):
    """Test case for issue_credential20_records_cred_ex_id_send_offer_post

    Send holder a credential offer in reference to a proposal with preview
    """
    body = openapi_server.V20CredBoundOfferRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/records/{cred_ex_id}/send-offer".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_records_cred_ex_id_send_request_post(client: TestClient):
    """Test case for issue_credential20_records_cred_ex_id_send_request_post

    Send issuer a credential request
    """
    body = openapi_server.V20CredRequestRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/records/{cred_ex_id}/send-request".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_records_cred_ex_id_store_post(client: TestClient):
    """Test case for issue_credential20_records_cred_ex_id_store_post

    Store a received credential
    """
    body = openapi_server.V20CredStoreRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/records/{cred_ex_id}/store".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_records_get(client: TestClient):
    """Test case for issue_credential20_records_get

    Fetch all credential exchange records
    """
    params = [("connection_id", 'connection_id_example'),     ("role", 'role_example'),     ("state", 'state_example'),     ("thread_id", 'thread_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/issue-credential-2.0/records",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_send_offer_post(client: TestClient):
    """Test case for issue_credential20_send_offer_post

    Send holder a credential offer, independent of any proposal
    """
    body = openapi_server.V20CredOfferRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/send-offer",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_send_post(client: TestClient):
    """Test case for issue_credential20_send_post

    Send holder a credential, automating entire flow
    """
    body = openapi_server.V20CredExFree()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/send",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_send_proposal_post(client: TestClient):
    """Test case for issue_credential20_send_proposal_post

    Send issuer a credential proposal
    """
    body = openapi_server.V20CredExFree()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/send-proposal",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential20_send_request_post(client: TestClient):
    """Test case for issue_credential20_send_request_post

    Send issuer a credential request not bound to an existing thread. Indy credentials cannot start at a request
    """
    body = openapi_server.V20CredRequestFree()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/send-request",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

