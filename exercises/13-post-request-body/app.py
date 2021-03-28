import requests
import json
request_body={
    "id":2323,
    "title":"Very big project"
}
headers={"Content-Type":"application/json"}

resp = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php", json=json.dumps(request_body),
    headers=headers)
print(resp.text)