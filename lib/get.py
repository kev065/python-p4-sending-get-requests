python3
import requests
pip3 install requests
url = "https://learn-co-curriculum.github.io/json-site-example/"
response = requests.get(url)
print(response.text)


import requests
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"
response = requests.get(url)
print(response.content)
import json
json.loads(response.content)
json_content = json.loads(response.text)
print(json.dumps(json_content, indent=4, sort_keys=True))