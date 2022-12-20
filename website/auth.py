from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)
    return render_template("login.html", text="Testing")

@auth.route('/logut')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up',  methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('firstName')
        from website import User
        user = User.query.filter_by(email=email).first()
        if not user:
            from . import db
            new_user = User(email=email, first_name=first_name, password=password)
            db.session.add(new_user)
            db.session.commit()
    return render_template("home.html")

