# import Flask class. (or not, says the squiggly line)
# and render_template method
from flask import Flask, render_template
from views import my_view


# app is an object of class type 'Flask'
app = Flask(__name__)
app.register_blueprint(my_view)

@app.errorhandler(404)
def page_not_found(e): # e = the exception raised. 
  return render_template("404.html", e=e)


# # this is a 'decorator'
# # if someone GET's '/'
# @app.route('/')
# # this function runs
# def index():
#   # return '<h1>Ello world!</h1>'
#   return render_template("index.html") # return the file 'templates/index.html'


# @app.route('/iain')
# def iain():
#   #return "<h1>Iain was here</h1>"
#   return render_template("iainwashere.html")



# this always goes last
if __name__ == "__main__":
  app.run(debug=True, port=8000)

