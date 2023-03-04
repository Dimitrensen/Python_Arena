from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

class UrlShortener:
    def __init__(self, long_url, short_url):
        self.long_url=long_url
        self.short_url=short_url

urls = []

# @app.route('/shorten', methods=['POST'])
# def shorten_url():
#     long_url = request.json['url']
#     short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
## I don't understand the line above.
#     url = UrlShortener(long_url, short_url)
#     urls.append(url)
#     return jsonify({'short_url': short_url})

# @app.route('/<short_url>', methods=['GET'])
# def redirect_to_long(short_url):
#     for url in urls:
#         if url.short_url == short_url:
#             return jsonify({'long_url': url.long_url})
#     return jsonify({'error': 'Short URL not found'})

# if __name__ == '__main__':
#     app.run(debug=True)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['url']
    while True:
        # generate random short url
        short_url = str(random.randint(1, 999999999))
        # check if short url already exists
        if not any(url.short_url == short_url for url in urls):
            # create url object and add to database
            url = UrlShortener(long_url, short_url)
            urls.append(url)
            return jsonify({'short_url': short_url})

# @app.route('/shorten, methods=['POST']')
# def shorten_url():
#     long_url = request.json['url']
#     #see where the latest number was and take it from there

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long(short_url):
    # look up original url in database
    for url in urls:
        if url.short_url == short_url:
            return jsonify({'long_url': url.long_url})
    # if short url not found
    return jsonify({'error': 'Short URL not found'})

if __name__ == '__main__':
    app.run(debug=True)
    