from flask import Flask, render_template

#create Flask data
BM = Flask(__name__)
BM.config['TEMPLATES_AUTO_RELOAD'] = True
#create a route decorator
@BM.route('/')
# shh file .shh_flask
#def index():
#    return "<h1> Welcome to Bifunctional Modalities Database!</h1>"def index():
def index():
    first = "Bifunctional"
    return render_template("index.html", first_name=first)

@BM.route('/user/<name>')
def user(name):
    return render_template ("user.html", user_name=name)

@BM.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
@BM.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500








if __name__ == '__main__':
    BM.run(debug=True)

