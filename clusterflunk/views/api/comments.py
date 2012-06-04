from pyramid.view import view_config
from datetime import datetime
from clusterflunk.models.comments import Comment
from clusterflunk.models.comments import CommentHistory
from clusterflunk.models.posts import PostComment
from clusterflunk.models.statuses import (
    Status,
    StatusComment
)
from clusterflunk.models.notifications import (
    Notification,
    StatusCommentNotification
)


@view_config(
    route_name='comments_post',
    renderer='json',
    request_method='POST',
    permission='view')
def post_add(request):
    db = request.db
    user = request.user

    post_id = request.json_body['post_id']
    parent_id = request.json_body['parent_id']
    body = request.json_body['body']

    # Replying to a comment
    if parent_id:
        comment_rev = CommentHistory(revision=1,
                                     created=datetime.now(),
                                     author_id=user.id,
                                     body=body)
        comment = Comment(parent_id=parent_id,
                          founder_id=user.id,
                          created=datetime.now(),
                          history=[comment_rev])

        db.add(comment)
    # Replying to a post
    else:
        comment_rev = CommentHistory(revision=1,
                                     created=datetime.now(),
                                     author_id=user.id,
                                     body=body)
        comment = Comment(parent_id=None,
                          founder_id=user.id,
                          created=datetime.now(),
                          history=[comment_rev])
        db.add(comment)
        db.flush()

        post_comment = PostComment(post_id=post_id,
                                   comment_id=comment.id)
        db.add(post_comment)
        db.add(comment_rev)

    db.flush()
    return {'id': comment.id,
            'post_id': post_id,
            'parent_id': comment.parent_id,
            'body': comment.history[0].body,
            'created_timedelta': comment.created_timedelta,
            'username': comment.founder.username}


@view_config(
    route_name='comments_status',
    renderer='json',
    request_method='POST',
    permission='view')
def status_add(request):
    db = request.db
    user = request.user

    status_id = request.json_body['status_id']
    body = request.json_body['body']
    status = db.query(Status).filter_by(id=status_id).first()

    comment_rev = CommentHistory(revision=1,
                                 created=datetime.now(),
                                 author_id=user.id,
                                 body=body)
    comment = Comment(founder_id=user.id,
                      history=[comment_rev],
                      created=datetime.now())

    db.add(comment)
    db.flush()

    status_comment = StatusComment(status_id=status_id,
                                   comment_id=comment.id)
    db.add(status_comment)

    # Create a notification, that can be sent to users who need to know about a
    # status being commented on.
    status_comment_notification = StatusCommentNotification(created=datetime.now(),
                                                            discriminator="status_comment",
                                                            user_id=user.id,
                                                            comment_id=comment.id,
                                                            status_id=status_id)
    # Notify the creator of the status that their status has been commented on.
    notification = Notification(user_id=status.founder.id,
                                notification_item=status_comment_notification)

    db.add(status_comment_notification)
    db.add(notification)
    db.flush()
    return {'id': comment.id,
            'body': comment.history[0].body,
            'status_id': status_id,
            'created_timedelta': comment.created_timedelta,
            'username': comment.history[0].author.username}
