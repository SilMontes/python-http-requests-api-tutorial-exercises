import requests

# your code here
response=requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
proyects = response.json()
last_proyect=proyects[-1]
images=last_proyect["images"]
print(images[-1])
first_proyect=proyects[0]
images2=first_proyect["images"]
print(images2[0])