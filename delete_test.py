import requests
import pytest

url = "https://jsonplaceholder.typicode.com/posts/1"


def test_statuse_code():
    response = requests.delete(url)
    assert response.status_code == 200

def  test_delete_or_not():
    response = requests.delete(url)
    res = response.json()
    assert  res == {}
