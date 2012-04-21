from wtforms import Form,\
                    SelectField,\
                    TextField,\
                    IntegerField,\
                    PasswordField,\
                    TextAreaField,\
                    validators
from wtforms.validators import ValidationError
from clusterflunk.models.users import User

class LoginForm(Form):
    username = TextField('Username',
                         [validators.Length(min=4, max=50),
                         validators.required()],
                         default="Username")
    password = PasswordField('Password',
                             [validators.required()])

class RegisterForm(Form):
    def __init__(form, db, *args, **kwargs):
        Form.__init__(form, *args, **kwargs)
        form.db = db

    username = TextField('Username',
                         [validators.Length(min=4, max=50),
                         validators.required()],
                         default="Username")
    email = TextField('E-mail',
                      [validators.Email("E-mail is of the incorrect format."),
                      validators.required()],
                      default="Email")
    password = PasswordField('Password',
                             [validators.required()])
    repeat_password = PasswordField('Repeat Password',
                                    [validators.required()])
    
    def validate_repeat_password(form, field):
        if form.password.data != field.data:
            raise ValidationError('The passwords do not match.')
    
    def validate_username(form, field):
        username_ok = form.db.query(User).filter_by(username=field.data).first()
        if username_ok is not None:
            raise ValidationError('That username is already taken.')

class CreateGroupForm(Form):
    name = TextField('Name',
                     [validators.Length(min=4, max=50),
                     validators.required()],
                     default="Name")
    description = TextAreaField('Description',
                                [validators.Length(min=4, max=50),
                                validators.required()],
                                default="Description")