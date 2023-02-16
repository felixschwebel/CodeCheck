from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap5
from flask_codemirror import CodeMirror
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os


# ------- FlaskForms -------
class CodeForm(FlaskForm):
    source_code = CodeMirrorField(language='python', config={'lineNumbers': 'true'})
    submit = SubmitField('Submit')

# mandatory
CODEMIRROR_LANGUAGES = ['python', 'yaml', 'htmlembedded']
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret'
# optional
CODEMIRROR_THEME = 'darcula'
CODEMIRROR_ADDONS = (('ADDON_DIR', 'ADDON_NAME'),)

# ------- Flask App -------
app = Flask(__name__)
bootstrap = Bootstrap5()
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config.from_object(__name__)
codemirror = CodeMirror(app)


# login_manager = LoginManager()
# login_manager.init_app(app)


@app.route("/")
def home():
    return render_template('account.html')


@app.route("/codecheck", methods=['GET', 'POST'])
def codecheck():
    code_form = CodeForm()
    if code_form.validate_on_submit():
        text = code_form.source_code.data
        print(text)
    return render_template('codecheck.html', code_form=code_form)


if __name__ == '__main__':
    app.run(debug=True)
