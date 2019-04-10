import json
import jsonpath
import requests

url = "http://petstore.swagger.io/v2/pet/50833"
response = requests.get(url)
# json_response = json.loads(response.text)

# pretty_data = json.dumps(json_response, indent=1)

# print(response)
#
# category_name = jsonpath.jsonpath(json_response, 'category.name')
# print(pretty_data)
# name = category_name[0]
# print(name)
#
# assert name == 'string'
print(response)
