import json

import jsonpath
import pytest
import requests


@pytest.mark.Smoke
def test_get_pet_with_id():
    url = "http://petstore.swagger.io/v2/pet/50833"
    response = requests.get(url)
    json_response = json.loads(response.text)

    pretty_data = json.dumps(json_response, indent=1)

    print(response)

    category_name = jsonpath.jsonpath(json_response, 'category.name')
    print(pretty_data)
    name = category_name[0]
    print(name)

    assert name == 'string'
    print(response)


def test_get_pet():
    param = {'status': 'pending'}

    uri = "http://petstore.swagger.io/v2/pet/findByStatus"

    response = requests.get(uri, params=param)
    json_response = json.loads(response.text)
    pretty_data = json.dumps(json_response, indent=1)
    print(response)

    pages = jsonpath.jsonpath(json_response, '0.category.id')
    print(pretty_data)
    print(pages)

    for i in range(0, 10):
        categoryId = jsonpath.jsonpath(json_response, '' + str(i) + '.category.id')
        print(categoryId)


@pytest.mark.Post
def test_post_pet():
    url = 'http://petstore.swagger.io/v2/pet'
    headers = {'Content-Type': 'application/json'}

    file = open('C:\\Users\\mdyuzhev\\PycharmProjects\\Integation\\resources\\createPet.json', 'r')
    json_input = file.read()
    print(json_input)
    request_json = json.loads(json_input)

    response = requests.post(url, data=json.dumps(request_json), headers=headers)
    print(response)


@pytest.mark.Post
def test_get_pet_with_myid():
    url = "http://petstore.swagger.io/v2/pet/117534423303"
    response = requests.get(url)
    json_response = json.loads(response.text)

    pretty_data = json.dumps(json_response, indent=1)

    print(response)

    category_name = jsonpath.jsonpath(json_response, 'category.name')
    print(pretty_data)
    name = category_name[0]
    print(name)

    assert name == 'MyTestPet'
    print(response)
