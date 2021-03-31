from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def getDbConnection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  
    return conn

@app.route('/')
def hello():
    conn = getDbConnection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)