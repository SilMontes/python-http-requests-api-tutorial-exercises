import requests

# your code her
url = "https://assets.breatheco.de/apis/fake/sample/post.php"
#item = {"code": 200, "message": "Successfuly added"}
request = requests.post(url)
print(request.text)