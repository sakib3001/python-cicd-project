import os
import sys
import pytest
from webee.app import app

# Add the src directory to the sys.path explicitly
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


@pytest.fixture
def client():
    """Fixture to provide a test client."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage(client):
    """
    Test if the homepage loads successfully and contains the expected content.
    """
    response = client.get("/")
    assert response.status_code == 200  # Check if the response is successful
    assert b"Inspirational Quotes" in response.data  # Check if the title is present
    assert b"Get a Quote" in response.data  # Check if the button text is present
    assert b"Made for Testing CI/CD v2" in response.data  # Check if the footer is present


def test_get_quote(client):
    """
    Test if the /get-quote endpoint returns a valid quote.
    """
    response = client.get("/get-quote")
    assert response.status_code == 200  # Check if the response is successful

    # Parse the JSON response
    json_data = response.get_json()
    assert "quote" in json_data  # Check if the "quote" key exists
    assert isinstance(json_data["quote"], str)  # Check if the quote is a string
    assert len(json_data["quote"]) > 0  # Check if the quote is not empty


def test_get_quote_randomness(client):
    """
    Test if the /get-quote endpoint returns different quotes on multiple requests.
    """
    quotes = set()
    for _ in range(5):  # Make 5 requests to check randomness
        response = client.get("/get-quote")
        assert response.status_code == 200
        json_data = response.get_json()
        quotes.add(json_data["quote"])  # Add the quote to the set

    # Check if at least two different quotes were returned
    assert len(quotes) > 1, "Quotes are not random enough"

# Add a newline at the end of the file
