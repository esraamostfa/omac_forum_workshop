from flask import render_template, request, redirect, url_for
import models
from app import app, members_store, posts_store

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = posts_store.get_all())

@app.route("/creat_topic.html", methods = ["GET", "POST"])
def creat_topic():
	if request.method == "POST":
		new_post = models.Post(request.form["title"], request.form["content"])
		posts_store.add(new_post)
		return redirect(url_for("home"))
	else:
		return render_template("creat_topic.html")