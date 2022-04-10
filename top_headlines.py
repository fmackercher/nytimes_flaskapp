
import requests
import json
from flask import Flask, render_template
from secrets import SECRET_KEY
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/<name>')
def name(name):
    return render_template('name.html', name=name)


@app.route('/headlines/<name>')
def headlines(name):
    news_api = requests.get(
        f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={SECRET_KEY}')

    top_headlines = news_api.json()
    top_articles = []

    for i in top_headlines['results']:
        top_articles.append(i['title'])

    return render_template('headline_list.html', tech_articles=top_articles[:5], name=name)


@app.route('/links/<name>')
def links(name):
    news_api = requests.get(
        f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={SECRET_KEY}')

    top_headlines = news_api.json()
    top_articles = []
    urls = []

    for i in top_headlines['results']:
        top_articles.append(i['title'])
        urls.append(i['url'])

    results = {}
    for key in top_articles[:5]:
        for value in urls:
            results[key] = value
            urls.remove(value)
            break
    return render_template('links.html', data=results.items(), name=name)


@app.route('/images/<name>')
def images(name):
    news_api = requests.get(
        f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={SECRET_KEY}')

    top_headlines = news_api.json()
    top_articles = []
    urls = []
    images = []
    for image in top_headlines['reults']:
        images.append(image['multimedia'][0]['url'])

    for i in top_headlines['results']:
        top_articles.append(i['title'])
        urls.append(i['url'])

    results = {}
    for key in top_articles[:5]:
        for value in urls:
            results[key] = value
            urls.remove(value)
            break
    return render_template('images.html', data=results.items(), images=images, name=name)


if __name__ == '__main__':
    print('starting nytimes app', app.name)
    app.run(debug=True)
