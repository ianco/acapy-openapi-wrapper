# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.admin_api_message_tracing import AdminAPIMessageTracing  # noqa: F401
from openapi_server.models.indy_cred_precis import IndyCredPrecis  # noqa: F401
from openapi_server.models.v20_pres_create_request_request import V20PresCreateRequestRequest  # noqa: F401
from openapi_server.models.v20_pres_ex_record import V20PresExRecord  # noqa: F401
from openapi_server.models.v20_pres_ex_record_list import V20PresExRecordList  # noqa: F401
from openapi_server.models.v20_pres_problem_report_request import V20PresProblemReportRequest  # noqa: F401
from openapi_server.models.v20_pres_proposal_request import V20PresProposalRequest  # noqa: F401
from openapi_server.models.v20_pres_send_request_request import V20PresSendRequestRequest  # noqa: F401
from openapi_server.models.v20_pres_spec_by_format_request import V20PresSpecByFormatRequest  # noqa: F401


def test_present_proof20_create_request_post(client: TestClient):
    """Test case for present_proof20_create_request_post

    Creates a presentation request not bound to any proposal or connection
    """
    body = openapi_server.V20PresCreateRequestRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/create-request",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_present_proof20_records_get(client: TestClient):
    """Test case for present_proof20_records_get

    Fetch all present-proof exchange records
    """
    params = [("connection_id", 'connection_id_example'),     ("role", 'role_example'),     ("state", 'state_example'),     ("thread_id", 'thread_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/present-proof-2.0/records",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_present_proof20_records_pres_ex_id_credentials_get(client: TestClient):
    """Test case for present_proof20_records_pres_ex_id_credentials_get

    Fetch credentials from wallet for presentation request
    """
    params = [("count", 'count_example'),     ("extra_query", 'extra_query_example'),     ("referent", 'referent_example'),     ("start", 'start_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/present-proof-2.0/records/{pres_ex_id}/credentials".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_present_proof20_records_pres_ex_id_delete(client: TestClient):
    """Test case for present_proof20_records_pres_ex_id_delete

    Remove an existing presentation exchange record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/present-proof-2.0/records/{pres_ex_id}".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_present_proof20_records_pres_ex_id_get(client: TestClient):
    """Test case for present_proof20_records_pres_ex_id_get

    Fetch a single presentation exchange record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/present-proof-2.0/records/{pres_ex_id}".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_present_proof20_records_pres_ex_id_problem_report_post(client: TestClient):
    """Test case for present_proof20_records_pres_ex_id_problem_report_post

    Send a problem report for presentation exchange
    """
    body = openapi_server.V20PresProblemReportRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/records/{pres_ex_id}/problem-report".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_present_proof20_records_pres_ex_id_send_presentation_post(client: TestClient):
    """Test case for present_proof20_records_pres_ex_id_send_presentation_post

    Sends a proof presentation
    """
    body = openapi_server.V20PresSpecByFormatRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/records/{pres_ex_id}/send-presentation".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_present_proof20_records_pres_ex_id_send_request_post(client: TestClient):
    """Test case for present_proof20_records_pres_ex_id_send_request_post

    Sends a presentation request in reference to a proposal
    """
    body = openapi_server.AdminAPIMessageTracing()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/records/{pres_ex_id}/send-request".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_present_proof20_records_pres_ex_id_verify_presentation_post(client: TestClient):
    """Test case for present_proof20_records_pres_ex_id_verify_presentation_post

    Verify a received presentation
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/records/{pres_ex_id}/verify-presentation".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_present_proof20_send_proposal_post(client: TestClient):
    """Test case for present_proof20_send_proposal_post

    Sends a presentation proposal
    """
    body = openapi_server.V20PresProposalRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/send-proposal",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_present_proof20_send_request_post(client: TestClient):
    """Test case for present_proof20_send_request_post

    Sends a free presentation request not bound to any proposal
    """
    body = openapi_server.V20PresSendRequestRequest()

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/send-request",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

