<%namespace name="header" file="header.mako"/>
<%namespace name="footer" file="footer.mako"/>
<!-- base.mako --> 
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" type="text/css" href="${request.static_url('clusterflunk:static/css/reset.css')}" />
        <link rel="stylesheet" type="text/css" href="${request.static_url('clusterflunk:static/css/style.css')}" />
        <link rel="stylesheet" type="text/css" href="${request.static_url('clusterflunk:static/css/type.css')}" />

        <!-- Third-Party Libraries -->
        <script src="${request.static_url('clusterflunk:static/js/libs/jquery-1.7.1.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/underscore.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/backbone.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/handlebars.js')}"></script>

        <!-- The Frontend -->
        <script src="${request.static_url('clusterflunk:static/js/index.js')}"></script>
    </head>
    <body>
        <div class="header">
            ${header.header(here)}
        </div>
        <div class="body">
            <div class="side">
                ${self.side()}
            </div>
            ${self.body()}
        </div>
        <div class="footer">
            ${footer.footer()}
        </div>
    </body>
</html>