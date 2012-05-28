from datetime import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember
from pyramid.security import forget
from clusterflunk.forms import LoginForm
from clusterflunk.forms import RegisterForm
from clusterflunk.models.users import User
from clusterflunk.models.auth import AuthUser


@view_config(route_name='login', renderer='clusterflunk:templates/auth/login.mako', permission='everyone')
def login(request):
    title = "Login"
    db = request.db

    login_form = LoginForm(request.POST)

    if request.method == 'POST' and 'submit' in request.POST and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data

        # Get user
        auth_user = db.query(AuthUser).filter_by(username=username).first()
        if auth_user and auth_user.validate_password(password):
            remember(request, auth_user.user.id)
            return HTTPFound(location="/")
        else:
            login_form.errors['password'] = ['Incorrect password.']

    return {'title': title,
            'login_form': login_form}


@view_config(route_name='register', renderer='clusterflunk:templates/auth/register.mako', permission='everyone')
def register(request):
    title = "Register"
    db = request.db

    register_form = RegisterForm(db, request.POST)

    if request.method == 'POST' and 'submit' in request.POST and register_form.validate():
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data

        # Add user
        user = User(username=username,
                    email=email,
                    joined=datetime.now(),
                    last_online=datetime.now())
        # Add auth user
        auth_user = AuthUser(username, password)
        user.auth_user = auth_user

        db.add(user)
        db.flush()

        remember(request, auth_user.user.id)
        return HTTPFound(location="/")

    return {'title': title,
            'register_form': register_form}


@view_config(route_name='logout', permission='everyone')
def logout(request):
    forget(request)
    return HTTPFound(location='/')
