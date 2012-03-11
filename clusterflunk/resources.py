from pyramid.security import Allow, Everyone, Authenticated

class Site(object):
    __acl__ = [(Allow, Everyone, 'everyone'),
               (Allow, Authenticated, 'view')]

    def __init__(self, request):
        pass