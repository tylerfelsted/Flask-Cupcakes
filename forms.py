from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired

class NewCupcakeForm(FlaskForm):
    """form for making a new cupcake"""

    flavor = StringField("Flavor")
    size = SelectField("Size", choices=[("small", "small"), ("medium", "medium"), ("large", "large"), ("jumbo", "jumbo")])
    rating = FloatField("Rating")
    image = StringField("Image URL")