from flask import Flask, jsonify, redirect, request
import random
import string

app = Flask(__name__)

class UrlShortener:
    def __init__(self, long_url, short_url):
        self.long_url=long_url
        self.short_url=short_url

urls = []

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['url']
        # generate random short url
    short_url = str(random.randint(1, 999999999))
        # create url object and add to database
    url = UrlShortener(long_url, short_url)
    urls.append(url)
    return url.__dict__


@app.route('/<short_url>', methods=['GET'])
def redirect_to_long(short_url):
    # look up original url in database
    for url in urls:
        if url.short_url == short_url:
            return redirect(url.long_url, code=302)
    # if short url not found
    return jsonify({'error': 'Short URL not found'})

if __name__ == '__main__':
    app.run(debug=True)
    