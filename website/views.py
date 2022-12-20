from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


@views.route('/login')
def login():
    # data = request.form
    # print(data)
    return render_template("login.html", text="Testing")
