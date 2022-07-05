from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)


@my_view.route('/')
# this function runs
def index():
  # return '<h1>Ello world!</h1>'
  return render_template("index.html") # return the file 'templates/index.html'


@my_view.route('/iain')
def iain():
  #return "<h1>Iain was here</h1>"
  return render_template("iainwashere.html")


@my_view.route('/about')
def about():
  return render_template("about.html")


@my_view.route('/aboutme')
def about_redirect(): # redirects one page/url to another
  return redirect(url_for("my_view.about"))