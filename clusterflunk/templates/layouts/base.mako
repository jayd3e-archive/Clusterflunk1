<%namespace name="header" file="header.mako"/>
<!-- base.mako -->
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.css" />
    </head>
    <body>
        <div class="top">
            <header class="header">
                ${ header.header(here) }
            </header>
        </div>
        <div class="page">
            ${ self.page() }
        </div>
    </body>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/libs/jquery-1.7.2.min.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/libs/jquery.masonry.min.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('clusterflunk:static/js/wireframes.js')}"></script>
</html>