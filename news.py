from config import config

import requests
from pathlib import Path
from GoogleNews import GoogleNews
googlenews = GoogleNews(lang="en")

topic_id = {
    "Headlines": ("CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSFFpZ0FQAQ", "#8BB8F8"),
    "World": ("CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSFFpZ0FQAQ", "#689F38"),
    "Technology": ("CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSFFpZ0FQAQ", "#039BE5"),
    "Entertainment": ("CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSFFpZ0FQAQ", "#7E57C2"),
    "Sports": ("CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSFFpZ0FQAQ", "#EF6C00"),
    "Science": ("CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKSFFpZ0FQAQ", "#E91E63"),
    "Health": ("CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE", "#5677FC"),
}

def get_news(topic: str, id_used: bool) -> list:
    try:
        if id_used:
            googlenews.set_topic(topic)
        else:
            googlenews.set_topic(topic_id[topic][0])
    except KeyError:
        return ["Invalid topic."]
    googlenews.get_news()
    results = googlenews.results()[:30]
    for story in results:
        if story["img"] != None:
            img = story["img"]
            img = requests.get(img, verify=config["verify_certs"]).url
            story["img"] = img
        if Path(f"static/media/{story['media']}.png").exists():
            story["mediaFavicon"] = f"/static/media/{story['media']}.png"
        else:
            story["mediaFavicon"] = None
    googlenews.clear()
    return results

def search_news(query):
    googlenews.get_news(query)
    results = googlenews.results()[:30]
    for story in results:
        if story["img"] != None:
            img = story["img"]
            img = requests.get(img, verify=config["verify_certs"]).url
            story["img"] = img
        if Path(f"static/media/{story['media']}.png").exists():
            story["mediaFavicon"] = f"/static/media/{story['media']}.png"
        else:
            story["mediaFavicon"] = None
    googlenews.clear()
    return results
