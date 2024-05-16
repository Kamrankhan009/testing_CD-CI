import pytest
import requests


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
