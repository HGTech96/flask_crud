from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    # data = request.form
    # print(data)
    return render_template("login.html", text="Testing")

@auth.route('/logut')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up')
def sign_up():
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     first_name = request.form.get('firstName')
    #     password1 = request.form.get('password1')
    #     password2 = request.form.get('password2')
    #
    #     if len(email) < 4:
    #         flash('Email must be greater than 4 characters.', category='error')
    #     elif len(first_name) < 2:
    #         pass
    #     elif password2 != password1:
    #         pass
    #     else:
    #         # add user
    #         pass

    return render_template("sign_up.html")

