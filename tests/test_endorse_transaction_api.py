# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.date import Date  # noqa: F401
from openapi_server.models.endorser_info import EndorserInfo  # noqa: F401
from openapi_server.models.transaction_jobs import TransactionJobs  # noqa: F401
from openapi_server.models.transaction_list import TransactionList  # noqa: F401
from openapi_server.models.transaction_record import TransactionRecord  # noqa: F401


def test_transaction_tran_id_resend_post(client: TestClient):
    """Test case for transaction_tran_id_resend_post

    For Author to resend a particular transaction request
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transaction/{tran_id}/resend".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_transactions_conn_id_set_endorser_info_post(client: TestClient):
    """Test case for transactions_conn_id_set_endorser_info_post

    Set Endorser Info
    """
    params = [("endorser_did", 'endorser_did_example'),     ("endorser_name", 'endorser_name_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{conn_id}/set-endorser-info".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_transactions_conn_id_set_endorser_role_post(client: TestClient):
    """Test case for transactions_conn_id_set_endorser_role_post

    Set transaction jobs
    """
    params = [("transaction_my_job", 'transaction_my_job_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{conn_id}/set-endorser-role".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_transactions_create_request_post(client: TestClient):
    """Test case for transactions_create_request_post

    For author to send a transaction request
    """
    body = '2013-10-20'
    params = [("tran_id", 'tran_id_example'),     ("endorser_write_txn", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/create-request",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_transactions_get(client: TestClient):
    """Test case for transactions_get

    Query transactions
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/transactions",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_transactions_tran_id_cancel_post(client: TestClient):
    """Test case for transactions_tran_id_cancel_post

    For Author to cancel a particular transaction request
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{tran_id}/cancel".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_transactions_tran_id_endorse_post(client: TestClient):
    """Test case for transactions_tran_id_endorse_post

    For Endorser to endorse a particular transaction record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{tran_id}/endorse".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_transactions_tran_id_get(client: TestClient):
    """Test case for transactions_tran_id_get

    Fetch a single transaction record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/transactions/{tran_id}".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_transactions_tran_id_refuse_post(client: TestClient):
    """Test case for transactions_tran_id_refuse_post

    For Endorser to refuse a particular transaction record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{tran_id}/refuse".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_transactions_tran_id_write_post(client: TestClient):
    """Test case for transactions_tran_id_write_post

    For Author / Endorser to write an endorsed transaction to the ledger
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{tran_id}/write".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

