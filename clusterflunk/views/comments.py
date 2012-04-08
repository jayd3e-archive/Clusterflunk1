from pyramid.view import view_config
from datetime import datetime
from clusterflunk.models.comments import Comment
from clusterflunk.models.comments import CommentHistory
from clusterflunk.models.posts import PostHistory

@view_config(
    route_name='comments_view',
    renderer='json',
    request_method='POST',
    permission='view')
def add(request):
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