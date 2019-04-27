from flask import Flask, request, redirect, jsonify, url_for
from load_articles import loadArticles
from config import POCKET_KEY, ACCESS_TOKEN

app = Flask(__name__)

@app.route('/tracks')
def getTracks():
    # articles = loadArticles()
    # for article in articles:
    #     print (article)
    return jsonify(articles)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
