import  requests
import pytest

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
res = response.json()
for i in  range(len(res)):
    def test_get_users_id():
        response = requests.get(url)
        res = response.json()
        assert res[i]["id"] != int

    def test_get_users_name():
        response = requests.get(url)
        res = response.json()
        assert res[i]['name'] != ""


    def test_get_users_usersname():
        response = requests.get(url)
        res = response.json()
        assert res[i]['username'] != ""


    def test_get_users_email():
        response = requests.get(url)
        res = response.json()
        assert res[i]['email'] != ""


    def test_get_users_address_street():
        response = requests.get(url)
        res = response.json()
        assert res[i]["address"]["street"] != ""

    def test_get_users_address_suite():
        response = requests.get(url)
        res = response.json()
        assert res[i]["address"]["suite"] != ""

    def test_get_users_address_city():
        response = requests.get(url)
        res = response.json()
        assert res[i]["address"]["city"] != ""

    def test_get_users_address_zipcode():
        response = requests.get(url)
        res = response.json()
        assert res[i]["address"]["zipcode"] != ""

    def test_get_users_address_geo_lat():
        response = requests.get(url)
        res = response.json()
        assert res[i]["address"]["geo"]["lat"] != str(int)

    def test_get_users_address_geo_lng():
        response = requests.get(url)
        res = response.json()
        assert res[i]["address"]["geo"]["lng"] != str(int)


    def test_get_users_phone():
        response = requests.get(url)
        res = response.json()
        assert res[i]["phone"] != str(int)

    def test_get_users_website():
        response = requests.get(url)
        res = response.json()
        assert res[i]["website"] != ""

    def test_get_users_company_name():
        response = requests.get(url)
        res = response.json()
        assert res[i]["company"]["name"] != ""

    def test_get_users_company_catchPhrase():
        response = requests.get(url)
        res = response.json()
        assert res[0]["company"]["catchPhrase"] != ""

    def test_get_users_company_bs():
        response = requests.get(url)
        res = response.json()
        assert res[i]["company"]["bs"] != ""