import requests

def get_post_tags(post_id):
    # request
    response=requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    data=response.json()
    posts=data["posts"]
    for post in posts:
        for element in post:
            if element == "id":
                if post[element] == post_id:
                    return post["tags"]
    #return None


print(get_post_tags(146))