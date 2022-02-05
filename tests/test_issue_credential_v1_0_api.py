# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.v10_credential_bound_offer_request import V10CredentialBoundOfferRequest  # noqa: F401
from openapi_server.models.v10_credential_conn_free_offer_request import V10CredentialConnFreeOfferRequest  # noqa: F401
from openapi_server.models.v10_credential_create import V10CredentialCreate  # noqa: F401
from openapi_server.models.v10_credential_exchange import V10CredentialExchange  # noqa: F401
from openapi_server.models.v10_credential_exchange_list_result import V10CredentialExchangeListResult  # noqa: F401
from openapi_server.models.v10_credential_free_offer_request import V10CredentialFreeOfferRequest  # noqa: F401
from openapi_server.models.v10_credential_issue_request import V10CredentialIssueRequest  # noqa: F401
from openapi_server.models.v10_credential_problem_report_request import V10CredentialProblemReportRequest  # noqa: F401
from openapi_server.models.v10_credential_proposal_request_mand import V10CredentialProposalRequestMand  # noqa: F401
from openapi_server.models.v10_credential_proposal_request_opt import V10CredentialProposalRequestOpt  # noqa: F401
from openapi_server.models.v10_credential_store_request import V10CredentialStoreRequest  # noqa: F401


def test_issue_credential_create_offer_post(client: TestClient):
    """Test case for issue_credential_create_offer_post

    Create a credential offer, independent of any proposal or connection
    """
    body = openapi_server.V10CredentialConnFreeOfferRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/create-offer",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_create_post(client: TestClient):
    """Test case for issue_credential_create_post

    Send holder a credential, automating entire flow
    """
    body = openapi_server.V10CredentialCreate()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/create",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_records_cred_ex_id_delete(client: TestClient):
    """Test case for issue_credential_records_cred_ex_id_delete

    Remove an existing credential exchange record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/issue-credential/records/{cred_ex_id}".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_records_cred_ex_id_get(client: TestClient):
    """Test case for issue_credential_records_cred_ex_id_get

    Fetch a single credential exchange record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/issue-credential/records/{cred_ex_id}".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_records_cred_ex_id_issue_post(client: TestClient):
    """Test case for issue_credential_records_cred_ex_id_issue_post

    Send holder a credential
    """
    body = openapi_server.V10CredentialIssueRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/records/{cred_ex_id}/issue".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_records_cred_ex_id_problem_report_post(client: TestClient):
    """Test case for issue_credential_records_cred_ex_id_problem_report_post

    Send a problem report for credential exchange
    """
    body = openapi_server.V10CredentialProblemReportRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/records/{cred_ex_id}/problem-report".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_records_cred_ex_id_send_offer_post(client: TestClient):
    """Test case for issue_credential_records_cred_ex_id_send_offer_post

    Send holder a credential offer in reference to a proposal with preview
    """
    body = openapi_server.V10CredentialBoundOfferRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/records/{cred_ex_id}/send-offer".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_records_cred_ex_id_send_request_post(client: TestClient):
    """Test case for issue_credential_records_cred_ex_id_send_request_post

    Send issuer a credential request
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/records/{cred_ex_id}/send-request".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_records_cred_ex_id_store_post(client: TestClient):
    """Test case for issue_credential_records_cred_ex_id_store_post

    Store a received credential
    """
    body = openapi_server.V10CredentialStoreRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/records/{cred_ex_id}/store".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_records_get(client: TestClient):
    """Test case for issue_credential_records_get

    Fetch all credential exchange records
    """
    params = [("connection_id", 'connection_id_example'),     ("role", 'role_example'),     ("state", 'state_example'),     ("thread_id", 'thread_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/issue-credential/records",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_send_offer_post(client: TestClient):
    """Test case for issue_credential_send_offer_post

    Send holder a credential offer, independent of any proposal
    """
    body = openapi_server.V10CredentialFreeOfferRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/send-offer",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_send_post(client: TestClient):
    """Test case for issue_credential_send_post

    Send holder a credential, automating entire flow
    """
    body = openapi_server.V10CredentialProposalRequestMand()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/send",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_send_proposal_post(client: TestClient):
    """Test case for issue_credential_send_proposal_post

    Send issuer a credential proposal
    """
    body = openapi_server.V10CredentialProposalRequestOpt()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/send-proposal",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

