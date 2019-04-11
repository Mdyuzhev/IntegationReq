import json
import jsonpath
import requests

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

