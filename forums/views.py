from flask import render_template
import models
from app import app, members_store, posts_store

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = posts_store.get_all())