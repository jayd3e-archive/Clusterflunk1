s<%namespace name="header" file="header.mako"/>
<%namespace name="footer" file="footer.mako"/>
<!-- base.mako --> 
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link href="${request.static_url('clusterflunk:static/css/screen.css')}" media="screen, projection" rel="stylesheet" type="text/css" />
        <link href="${request.static_url('clusterflunk:static/css/print.css')}" media="print" rel="stylesheet" type="text/css" />
        <!--[if lt IE 8]>
          <link href="${request.static_url('clusterflunk:static/css/ie.css')}" media="screen, projection" rel="stylesheet" type="text/css" />
        <![endif]-->

        <!-- Third-Party Libraries -->
        <script src="${request.static_url('clusterflunk:static/js/libs/jquery-1.7.1.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/jquery-ui-1.8.16.custom.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/underscore.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/backbone.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/handlebars.js')}"></script>

        <!-- The Frontend -->
        <script src="${request.static_url('clusterflunk:static/js/index.js')}"></script>
    </head>
    <body>
        <div id="wrap">
            <header id="header">
                ${header.header(here)}
            </header>
            <div id="page">
                <article>
                    ${self.page()}
                </article>
                <aside>
                    ${self.aside()}
                </aside>
            </div>
            <footer id="footer">
                ${footer.footer()}
            </footer>
        </div>
    </body>
</html>