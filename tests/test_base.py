import json

import jsonpath
import pytest
import requests

create_json = 'C:\\Users\\mdyuzhev\\PycharmProjects\\Integation\\resources\\createPet.json'


def create_body(path_for_message):
    file = open(path_for_message, 'r')
    json_input = file.read()
    body = json.loads(json_input)
    return body
