import requests

# your code here
response=requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
response_json=response.json()
#accesando a el nickname del autor
posts=response_json["posts"][0]["author"]["name"]
print(posts)
posteos=response_json["posts"]
for post in posteos:
    if "attachments" in post:
        if post["attachments"] != []:
            print("1111")
            print(post["attachments"][0]["images"]["thumbnail"]["url"])