from flask import Flask, render_template, request, redirect
import news

app = Flask(__name__)

settings = {
    "name": "News",
}

@app.route("/")
def index():
    topic = "Headlines"
    requested_news = news.get_news(topic, False)
    return render_template("home.html", name=settings["name"], news=requested_news, topic=topic, topic_color=news.topic_id[topic][1])

@app.route("/topic/<topic>")
def topic(topic):
    topic = topic.capitalize()
    requested_news = news.get_news(topic, False)
    if requested_news == ["Invalid topic."]:
        return redirect("/")
    return render_template("home.html", name=settings["name"], news=requested_news, topic=topic, topic_color=news.topic_id[topic][1])

@app.route("/topic/byId/<topic_id>")
def topic_by_id(topic_id):
    topic = topic_id
    requested_news = news.get_news(topic, True)
    if requested_news == ["Invalid topic."]:
        return redirect("/")
    return render_template("home.html", name=settings["name"], news=requested_news, topic="Custom Topic")

@app.route("/search")
def search():
    query = request.args.get("q")
    requested_news = news.search_news(query)
    return render_template("home.html", name=settings["name"], news=requested_news, topic="Custom Topic", query=query)

if __name__ == "__main__":
    app.run(debug=True)
