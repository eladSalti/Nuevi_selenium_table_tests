import requests
import pytest

BASE_URL = "http://localhost:3000"  # Replace with the actual base URL of your backend service



@pytest.mark.parametrize("transaction_id", [123, 456, 789])
def test_get_transaction(transaction_id):
    url = f"{BASE_URL}/transaction/{transaction_id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    # Add more assertions for validating the response data

def test_create_transaction():
    url = f"{BASE_URL}/transaction"
    payload = {
        "transactionMainID": 123,
        "transactionDate": "2023-05-22",
        "status": "pending",
        "clientId": 1,
        "amount": 100.0,
        "currencyCode": "USD",
        "bankName": "Example Bank",
        "dateModified": "2023-05-22",
        "dateCreated": "2023-05-22"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["status"] == "success"
    # Add more assertions or validation logic as needed

# Add more test functions for other API endpoints and scenarios
