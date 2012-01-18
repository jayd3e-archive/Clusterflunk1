from pyramid.security import (
    forget,
    remember,
)
from pyramid.view import view_config

@view_config(
    route_name='api.login',
    request_method='POST',
    renderer='json')
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == 'admin':
        userid = username
        headers = remember(request, userid)
        request.response.headerlist += headers
        return {
            'status': 'logged_in',
            'userid': userid,
        }
    return {
        'status': 'not_logged_in',
    }

@view_config(
    route_name='api.logout',
    renderer='json',
    permission='logged_in')
def logout_view(request):
    headers = forget(request)
    request.response.headerlist += headers
    return {
        'status': 'logged_out',
    }
