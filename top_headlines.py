
import requests
import json
from flask import Flask, render_template
from secrets import SECRET_KEY
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/headlines/<name>')
def headlines(name):
    news_api = requests.get(
        f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={SECRET_KEY}')

    top_headlines = news_api.json()
    top_articles = []

    for i in top_headlines['results']:
        top_articles.append(i['title'])

    return render_template('headline_list.html', tech_articles=top_articles[:5], name=name)


@app.route('/<name>')
def name(name):
    return render_template('name.html', name=name)


if __name__ == '__main__':
    print('starting nytimes app', app.name)
    app.run(debug=True)
