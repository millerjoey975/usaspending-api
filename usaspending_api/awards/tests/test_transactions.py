import pytest
from model_mommy import mommy
from rest_framework import status
import json


@pytest.mark.django_db
def test_transaction_endpoint(client):
    """Test the transaction endpoint."""

    resp = client.get('/api/v1/transactions/')
    assert resp.status_code == 200
    assert len(resp.data) > 2

    assert client.post(
        '/api/v1/transactions/?page=1&limit=4',
        content_type='application/json').status_code == 200


@pytest.mark.django_db
def test_transaction_endpoint_award_fk(client):
    """Test the transaction endpoint."""

    awd = mommy.make('awards.Award', id=10, total_obligation="2000", _fill_optional=True)
    mommy.make(
        'awards.Transaction',
        award=awd)

    assert client.post(
        '/api/v1/transactions/',
        content_type='application/json',
        data=json.dumps({
            "filters": [{
                "field": "award",
                "operation": "equals",
                "value": "10"
            }]
        })).status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_txn_total_grouped(client):
    """Test award total endpoint with a group parameter."""
    # add this test once the transaction backend is refactored
    pass


@pytest.mark.django_db
def test_txn_get_or_create():
    """Test Transaction.get_or_create method."""

    # if txn doesn't exist yet, create it

    # if txn already exists but has an action date < the incoming
    # last modified date, update the existing txn

    # if the txn already exists but has an action date > the incoming
    # last modified date, do nothing

    # if the txn already exists, does not have an action date and its
    # certified date < the incoming ???action or certified??? date, update
    # the existing txn

    # if the txn already exists, does not have an action date and its
    # certified date > the incoming ???action or certified??? date, do nothing
