from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SearchForm(Form):
	first_name = StringField('first_name', validators=[DataRequired()])