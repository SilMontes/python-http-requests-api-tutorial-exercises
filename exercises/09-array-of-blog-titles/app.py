import requests

def get_titles():
    # request
    response=requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    data=response.json()
    titles=[]
    posts=data["posts"]
    for post in posts:
        if "title" in post:
            titles.append(post["title"])

    return titles


print(get_titles())