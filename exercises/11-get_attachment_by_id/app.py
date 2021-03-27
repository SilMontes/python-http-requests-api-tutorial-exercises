import requests

def get_attachment_by_id(attachment_id):
    # your code here
    response=requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    data=response.json()
    posts=data["posts"]
    for post  in posts:  ## post = each post in posts dictionary
        for element in post:  ##each element(id, url, title) in each post
            if element == "attachments":
                for elementInAttachements in post[element]: ## elementInAttachements = each dictionary in each attachment
                        for item in elementInAttachements:  ## each item of each dictionary in each attachment
                            if item == "id":
                                if elementInAttachements[item] == attachment_id:
                                    #return elementInAttachements  returns the attatchement with the given id
                                    return elementInAttachements["title"] 
    

print(get_attachment_by_id(137))