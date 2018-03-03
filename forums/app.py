import models
import stores
import data
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = data.posts_store.get_all())

app.run()