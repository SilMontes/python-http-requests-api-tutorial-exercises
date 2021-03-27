import requests

# your code here
response=requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")
response_format= response.json()
#print(response_format["name"])
print("Response ", response_format)
images= response_format["images"]
print(images[1:])