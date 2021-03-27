import requests
import json
payload={
    "id":2323,
    "title":"Very big project"
}
headers={
    "Content-type":"application/json"
}
resp = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php",
    data=json.dumps(payload),
    headers=headers)
print(resp.text)