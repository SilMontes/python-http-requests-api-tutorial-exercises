import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
json_response=response.json()
hours=json_response["hours"]
minutes= json_response["minutes"]
seconds= json_response["seconds"]
current_time= "Current time: "+ str(hours)+" hrs "+str(minutes)+" min and "+str(seconds)+" sec"
print(current_time)