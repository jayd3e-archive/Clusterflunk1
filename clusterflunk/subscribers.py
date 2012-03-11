from pyramid.events import subscriber
from pyramid.events import BeforeRender

@subscriber(BeforeRender)
def add_globals(event):
    here = event['request'].environ['PATH_INFO']
    user = event['request'].user
    event['here'] = here
    event['user'] = user