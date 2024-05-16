import pytest
import requests

# By placing disable_network_calls() in conftest.py and adding the autouse=True option,
# you ensure that network calls will be disabled in every test across the suite.
# Any test that executes code calling requests.get() will raise a RuntimeError indicating that
# an unexpected network call would have occurred.
@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())
    
    
@pytest.fixture
def example_fixture():
    return 1


@pytest.fixture
def group_of_people():
    return  [
        {
            "given_name":"kamran khan",
            "family_name": "Bangash",
            "title": "Senior python developer"
        },
        {
            "given_name": "Somia Bangash",
            "family_name": "Bangash",
            "title": "Senior Laravell developer"
        }
    ]
