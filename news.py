import requests
from GoogleNews import GoogleNews
googlenews = GoogleNews(lang="en")

topic_id = {
    "Headlines": ("CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSFFpZ0FQAQ", "#8BB8F8"),
    "World": ("CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSFFpZ0FQAQ"),
    "Technology": ("CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSFFpZ0FQAQ"),
    "Entertainment": ("CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSFFpZ0FQAQ")
}

def get_news(topic: str) -> list:
    googlenews.set_topic(topic_id[topic][0])
    googlenews.get_news()
    results = googlenews.results()[:30]
    for story in results:
        if story["img"] != None:
            img = story["img"]
            img = requests.get(img).url
            story["img"] = img
    return results
