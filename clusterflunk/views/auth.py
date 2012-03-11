from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember
from pyramid.security import forget
from clusterflunk.forms import LoginForm
from clusterflunk.forms import RegisterForm
from clusterflunk.models.user import User

@view_config(route_name='login', renderer='auth/login.mako', permission='everyone')
def login(request):
    title = "Login"
    db = request.db

    login_form = LoginForm(request.POST)
    register_form = RegisterForm(db, request.POST)

    if request.method == 'POST' and 'login_submit' in request.POST and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data

        # Get user
        user = db.query(User).filter_by(username=username).first()
        if user and user.validate_password(password):
            remember(request, user.id)
            return HTTPFound(location="/")
        else:
            login_form.errors['password'] = ['Incorrect password.']

    if request.method == 'POST' and 'register_submit' in request.POST and register_form.validate():
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        
        # Add user
        user = User(username, password, email=email)
        db.add(user)
        db.flush()

        remember(request, user.id)
        return HTTPFound(location="/")

    return {'title':title,
            'login_form':login_form,
            'register_form':register_form}
    
@view_config(route_name='logout', permission='everyone')
def logout(request):
    request = self.request

    forget(request)
    return HTTPFound(location='/')