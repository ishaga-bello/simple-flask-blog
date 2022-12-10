from flask import Flask, render_template, flash, request, redirect, url_for
import sqlite3
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    
    return post

app = Flask(__name__)
# TODO:create an env file to store this
app.config['SECRET_KEY'] = "my_secret_123"

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()

    return render_template("index.html", posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)

    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('create.html')