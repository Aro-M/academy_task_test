import requests
import pytest

url = "https://jsonplaceholder.typicode.com/posts/2"

body = {
            "title" : "Make a Put call",
            "body" : "Details of making post call ....",
            "userId": 1
       }


def test_title():
    response = requests.put(url, data=body)
    res = response.json()
    assert res["title"] != ""


def test_id():
    response = requests.put(url, data=body)
    res = response.json()
    assert res["id"] != int

def test_body():
    response = requests.put(url, data=body)
    res = response.json()
    assert res["body"] != ""

def test_userId():
    response = requests.put(url, data=body)
    res = response.json()
    assert res["userId"] != str(int)

def test_statuse_code():
    response = requests.put(url, data=body)
    assert response.status_code == 200



response = requests.put(url, data=body)
print(response.json())