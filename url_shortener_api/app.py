from flask import Flask
import classes
import json
urls = []

app = Flask(__name__)

class UrlShortener:
    def __init__(self, long_url, short_url)
        self.long_url=long_url
        self.short_url=short_url

urls = []

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['url']
    short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url = UrlShortener(long_url, short_url)
    urls.append(url)
    return jsonify({'short_url': short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long(short_url):
    for url in urls:
        if url.short_url == short_url:
            return jsonify({'long_url': url.long_url})
    return jsonify({'error': 'Short URL not found'})

if __name__ == '__main__':
    app.run(debug=True)
    