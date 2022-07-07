from flask import Flask, render_template, Blueprint, redirect, url_for
my_view = Blueprint('my_view', __name__)

# return the site urls to the appropriate pages
@my_view.route('/')
def index():
  return render_template("index.html")

@my_view.route('/page1')
def page1():
  return render_template("page1.html")

@my_view.route('/page2')
def page2():
  return render_template("page2.html")

@my_view.route('/page3')
def page3():
  return render_template("page3.html")

@my_view.route('/page4')
def page4():
  return render_template("page4.html")

@my_view.route('/page5')
def page5():
  return render_template("page5.html")

# redirect a few pages the user should not have access to back to home page
@my_view.route('/js')
@my_view.route('/javascript')
@my_view.route('/home')
def general_redirects():
  # return render_template("index.html")
  return redirect(url_for("my_view.index"))
  # Second one is better, it also changes the url in the browser navbar

# 'secret' admin page, without an entry in the navbar. It doesn't have a user/password, but it doesn't have any content either
@my_view.route('/admin')
def admin_page():
  return render_template("admin.html")



