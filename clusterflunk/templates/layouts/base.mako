<%namespace name="header" file="header.mako"/>
<%namespace name="footer" file="footer.mako"/>
<!-- base.mako -->
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" type="text/css" href="${request.static_url('clusterflunk:static/slicknasty/css/bootstrap.css')}" />
        <link rel="stylesheet" type="text/css" href="${request.static_url('clusterflunk:static/css/bootstrap.css')}" />
    </head>
    <body>
        <div id="top">
            <div class="container">
                <header id="header">
                    ${header.header(here)}
                </header>
            </div>
        </div>
        <div id="main">
            <div class="container">
                <article id="page">
                    ${ self.page() }
                </article>
                <aside id="aside">
                    ${ self.aside() }
                </aside>
            </div>
        </div>
    </body>
    <!-- Third-Party Libraries -->
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/libs/jquery-1.7.1.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/libs/underscore.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/libs/backbone.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/libs/handlebars.js')}"></script>

    <!-- The Frontend -->
    <!-- Main App -->
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/index.js')}"></script>

    <!-- Modules -->
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/modules/comment.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/modules/post.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/modules/feed.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/modules/status.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/modules/feed.js')}"></script>
</html>