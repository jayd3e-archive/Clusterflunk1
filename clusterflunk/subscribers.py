from pyramid.events import subscriber
from pyramid.events import BeforeRender

@subscriber(BeforeRender)
def add_globals(event):
    user = event['request'].user
    db = event['request'].db
    event['user'] = user

    notifications = user.notifications

    event['notifications'] = notifications