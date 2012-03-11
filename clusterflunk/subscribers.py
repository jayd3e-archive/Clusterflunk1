from pyramid.events import subscriber
from pyramid.events import BeforeRender

@subscriber(BeforeRender)
def add_globals(event):
    user = event['request'].user
    event['user'] = user