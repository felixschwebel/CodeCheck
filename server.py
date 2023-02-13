from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

# ------- Flask App -------
app = Flask(__name__)
bootstrap = Bootstrap5()
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

# login_manager = LoginManager()
# login_manager.init_app(app)


@app.route("/")
def home():
    return render_template('account.html')


if __name__ == '__main__':
    app.run(debug=True)
