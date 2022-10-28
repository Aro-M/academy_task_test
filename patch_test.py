import requests
import pytest

url = "https://jsonplaceholder.typicode.com/posts/1"

body = {
            "title" : "Make a Put call",

       }


def test_title():
    response = requests.patch(url, data=body)
    res = response.json()
    assert res["title"] != ""


def test_id():
    response = requests.patch(url, data=body)
    res = response.json()
    assert res["id"] != int

def test_body():
    response = requests.patch(url, data=body)
    res = response.json()
    assert res["body"] != ""

def test_userId():
    response = requests.patch(url, data=body)
    res = response.json()
    assert res["userId"] != str(int)

def test_statuse_code():
    response = requests.patch(url, data=body)
    assert response.status_code == 200



response = requests.patch(url, data=body)
print(response.json())