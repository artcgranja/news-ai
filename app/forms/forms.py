from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ApiKeyForm(FlaskForm):
    api_key = StringField('OpenAI API Key', validators=[DataRequired()])
    submit = SubmitField('Save API Key') 