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

@view_config(
    route_name='articles_view',
    renderer='clusterflunk:templates/articles/view.mako',
    permission='view')
def view(request):
    db = request.db
    user = request.user
    _id = request.matchdict.get('article_id')

    article = db.query(Article).filter_by(id=_id).first()
    return {'article': article}