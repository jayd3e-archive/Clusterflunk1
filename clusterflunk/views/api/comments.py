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
    route_name='comments_post_view',
    renderer='json',
    request_method='POST',
    permission='view')
def post_add(request):
    db = request.db
    user = request.user

    post_id = request.POST['post_id']
    parent_id = request.POST['parent_id']
    body = request.POST['body']

    # Replying to a comment
    if parent_id:
        comment = Comment(parent_id=parent_id,
                          founder_id=user.id)
        db.add(comment)
        db.flush()

        comment_rev = CommentHistory(revision=1,
                                     created=datetime.now(),
                                     author_id=user.id,
                                     comment_id=comment.id,
                                     body=body)
        db.add(comment_rev)
    # Replying to a post
    else:
        comment = Comment(parent_id=None,
                          founder_id=user.id)
        db.add(comment)
        db.flush()

        post_comment = PostComment(post_id=post_id,
                                   comment_id=comment.id)
        comment_rev = CommentHistory(revision=1,
                                     created=datetime.now(),
                                     author_id=user.id,
                                     comment_id=comment.id,
                                     body=body)
        db.add(post_comment)
        db.add(comment_rev)
    
    db.flush()
    return {'id':comment.id,
            'post_id':0,
            'body':comment.history[0].body}

@view_config(
    route_name='comments_status_view',
    renderer='json',
    request_method='POST',
    permission='view')
def status_add(request):
    db = request.db
    user = request.user

    status_id = request.POST['status_id']
    body = request.POST['body']
    status = db.query(Status).filter_by(id=status_id).first()

    comment_rev = CommentHistory(revision=1,
                                 created=datetime.now(),
                                 author_id=user.id,
                                 body=body)
    comment = Comment(founder_id=user.id,
                      history=[comment_rev])
    
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
    notification = Notification(user_id=status.author.id,
                                notification_item=status_comment_notification)

    db.add(status_comment_notification)
    db.add(notification)
    db.flush()
    return {'id':comment.id,
            'body':comment.history[0].body}