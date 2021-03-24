from flask import Flask
from flask import request, Flask, render_template
from flask.helpers import make_response
from flask_bootstrap import Bootstrap 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard_to_guess'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html')
@app.route('/form1', methods=['GET', 'POST'])
def form_one():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('form1.html', form=form, name=name)
@app.route('/cookie')
def cookie():
    response = make_response('<h1> this document carries a cookie</h1>')
    response.set_cookie('answer', '42')
    return response


if __name__ == '__main__':
    app.run()