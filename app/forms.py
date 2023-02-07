from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import Application

import phonenumbers


class ApplicationForm(FlaskForm):

    username = StringField('Ваше имя', validators=[DataRequired()])
    body = TextAreaField('Комментарий', validators=[Length(min=0, max=140)])
    phone = StringField('Телефон', validators=[Length(min=9, max=20)])

    def validate_phone(self, phone):
        if len(phone.data) > 16:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(phone.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+7" + phone.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
