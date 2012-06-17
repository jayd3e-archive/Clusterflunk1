from pyramid.security import Allow, Everyone


class Site(object):
    __acl__ = [(Allow, Everyone, 'view')]

    def __init__(self, request):
        pass
