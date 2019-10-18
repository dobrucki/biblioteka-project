from . import auth
from flask import render_template, url_for
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    # user = User.query.filter_by(email=form.email.data).first()
    # if user is not None and user.verify_password(form.password.data):
    #         login_user(user, form.remember_me.data)
    # return redirect(request.args.get('next') or url_for('main.index')) flash('Invalid username or password.')
    return render_template('login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
