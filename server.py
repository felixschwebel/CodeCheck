from flask import Flask, render_template, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_codemirror import CodeMirror
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
import requests
import openai

# ---------------------------- CONFIGURATIONS ------------------------
# CodeMirror Settings
CODEMIRROR_LANGUAGES = ['python', 'java', 'C']
WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ['SECRET_KEY']
CODEMIRROR_THEME = 'darcula'
CODEMIRROR_ADDONS = (('ADDON_DIR', 'ADDON_NAME'),)


# LoginManager
# login_manager = LoginManager()
# login_manager.init_app(app)


# ---------------------------- FLASK-FORMS ----------------------------
class CodeForm(FlaskForm):
    source_code = CodeMirrorField(language='python', config={'lineNumbers': 'true'})
    submit = SubmitField('Submit')


# ---------------------------- FLASK APP ------------------------------
app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config.from_object(__name__)

# App Components
bootstrap = Bootstrap5(app)
codemirror = CodeMirror(app)


tiles = []


# ---------------------------- ROUTING --------------------------------
@app.route("/")
def home():
    return render_template('account.html')


@app.route("/codecheck", methods=['GET', 'POST'])
def codecheck():
    code_form = CodeForm()
    if code_form.validate_on_submit():

        # get the form parameters
        func_type = request.form.get('button-id')
        input_code = code_form.source_code.data

        # if input_code == '':
        #     flash('Sorry! There is no code here.')
        #     return render_template('codecheck.html', code_form=code_form)

        # code.explain() - function
        if func_type == 'FUNC-EXPLAIN':
            response = 'This explains the code.'
            tiles.append({'title': 'explain', 'content': response})

        # code.optimise() - function
        if func_type == 'FUNC-OPTIMISE':
            response = 'This optimises the code.'
            tiles.append({'title': 'optimise', 'content': response})

        # code.fix_bugs() - function
        if func_type == 'FUNC-BUG':
            response = 'This fixes bugs in the code.'
            tiles.append({'title': 'fix_bugs', 'content': response})

        # code.docs() - function
        if func_type == 'FUNC-DOC':
            response = 'This documents the code.'
            tiles.append({'title': 'docs', 'content': response})

        # code.convert() - function
        if func_type == 'FUNC-CONV':
            response = 'This converts the code.'
            tiles.append({'title': 'convert', 'content': response})

        return render_template('codecheck.html', code_form=code_form, tiles=tiles)

    return render_template('codecheck.html', code_form=code_form, tiles=tiles)


@app.route('/delete_tile', methods=['POST'])
def delete_tile():
    i = request.form['id']
    tiles.pop(int(i) - 1)
    return ''


# ---------------------------- RUN SERVER ------------------------------
if __name__ == '__main__':
    app.run(debug=True)

# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))
#
#     result = request.args.get("result")
#     return render_template("index.html", result=result)
#
#
# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.
#
# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
