from pyramid.view import view_config
from clusterflunk.models.articles import Article

@view_config(
    route_name='articles',
    renderer='clusterflunk:templates/articles/index.mako',
    permission='view')
def index(request):
    db = request.db
    user = request.user

    articles = db.query(Article).order_by(Article.created).all()
    return {'articles': articles}
