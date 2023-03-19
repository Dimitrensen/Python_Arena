from flask import Flask, jsonify
import sqlite3
import random

app = Flask(__name__)
app.config['DATABASE'] = 'passwords.db'

def get_db():
    """Returns a connection to the SQLite database."""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Creates the passwords table if it doesn't exist."""
    with app.app_context():
        db = get_db()
        db.execute('CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT)')
        db.commit()

init_db()

@app.route('/generate', methods=['POST'])
def generate_password():
    password = str(random.randint(100000000, 999999999))
    with app.app_context():
        db = get_db()
        db.execute('INSERT INTO passwords (password) VALUES (?)', (password,))
        db.commit()
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
