import requests

session = requests.Session()

startTitle = "cheese"
url = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "backlinks",
    "bltitle": startTitle,
    "blredirect": True
}

R = session.get(url=url, params=PARAMS)
DATA = R.json()
#print(DATA)

INFO = DATA["query"]["backlinks"]

BACKLINKS = [backlink["title"] for backlink in INFO]
print(BACKLINKS)