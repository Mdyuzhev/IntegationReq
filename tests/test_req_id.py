import json

import jsonpath
import pytest
import requests
from tests import test_base


@pytest.mark.Smoke
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
    body = json.loads(json_input)
    exp_name = jsonpath.jsonpath(body, 'category.name')[0]
    cat_name = jsonpath.jsonpath(body, 'category.name')[0]
    request_json = json.loads(json_input)

    response = requests.post(url, data=json.dumps(request_json), headers=headers)
    try:
        assert cat_name == exp_name
    except AssertionError as e:
        message = e.args[0]
        message += "\nСравнение прошло неуспешно"
        e.args = (message,)  # wrap it up in new tuple
        raise
    print(response)


@pytest.mark.Post
def test_get_pet_with_myid():
    url = "http://petstore.swagger.io/v2/pet/117534423303"
    response = requests.get(url)
    json_response = json.loads(response.text)
    pretty_data = json.dumps(json_response, indent=1)
    print(pretty_data)
    file = open('C:\\Users\\mdyuzhev\\PycharmProjects\\Integation\\resources\\createPet.json', 'r')
    json_input = file.read()
    body = json.loads(json_input)
    exp_name = jsonpath.jsonpath(body, 'category.name')[0]
    category_name = jsonpath.jsonpath(json_response, 'category.name')[0]

    try:
        assert category_name == exp_name
    except AssertionError as e:
        message = e.args[0]
        message += "\nСравнение прошло неуспешно"
        e.args = (message,)  # wrap it up in new tuple
        raise


@pytest.mark.Post
def test_put_pet():
    url = 'http://petstore.swagger.io/v2/pet'
    headers = {'Content-Type': 'application/json'}

    file = open('C:\\Users\\mdyuzhev\\PycharmProjects\\Integation\\resources\\putPet.json', 'r')
    json_input = file.read()
    body = json.loads(json_input)
    cat_id = jsonpath.jsonpath(body, 'category.id')[0]
    request_json = json.loads(json_input)

    response = requests.put(url, data=json.dumps(request_json), headers=headers)
    json_response = json.loads(response.text)
    category_id = jsonpath.jsonpath(json_response, 'category.id')[0]
    try:
        assert category_id == cat_id
    except AssertionError as e:
        message = e.args[0]
        message += "\nСравнение прошло неуспешно"
        e.args = (message,)  # wrap it up in new tuple
        raise


@pytest.mark.Smoke
def test_del_pet():
    url = "http://petstore.swagger.io/v2/pet/117534423303"
    response = requests.delete(url)
    print(response)
