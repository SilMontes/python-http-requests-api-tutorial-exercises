import requests

# your code here
response=requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
proyects = response.json()
proyect1 = proyects[1]
print(proyect1["name"])
proyects_names=[]
for proyect in proyects:
    proyects_names.append(proyect["name"])
print(proyects_names)
