from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'urls.db'

def get_db():
    db = sqlite3.connect(app.config['DATABASE'])
    db.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY AUTOINCREMENT, long_url TEXT, short_url TEXT)')
    return db

class UrlShortener:
    next_id = 1

    def __init__(self, long_url):
        self.long_url = long_url
        self.short_url = str(UrlShortener.next_id)
        UrlShortener.next_id += 1

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['url']
    db = get_db()
    cur = db.cursor()
    cur.execute('INSERT INTO urls (long_url, short_url) VALUES (?, ?)', (long_url, str(UrlShortener.next_id)))
    db.commit()
    url = UrlShortener(long_url)
    return jsonify({'short_url': url.short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long(short_url):
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT long_url FROM urls WHERE short_url = ?', (short_url,))
    result = cur.fetchone()
    if result:
        return jsonify({'long_url': result[0]})
    else:
        return jsonify({'error': 'Short URL not found'})

if __name__ == '__main__':
    app.run(debug=True)
