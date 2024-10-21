from flask import Flask, render_template, request
import news

app = Flask(__name__)

settings = {
    "name": "News",
}

@app.route("/")
def index():
    topic = "Headlines"
    requested_news = news.get_news(topic)
    return render_template("home.html", name=settings["name"], news=requested_news, topic=topic, topic_color=news.topic_id[topic][1])

if __name__ == "__main__":
    app.run(debug=True)
