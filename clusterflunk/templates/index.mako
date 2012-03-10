<!doctype html>
<html>
    <head>
        <title></title>

        <!-- Third-Party Libraries -->
        <script src="${request.static_url('clusterflunk:static/js/libs/jquery-1.7.1.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/underscore.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/backbone.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/backbone.layoutmanager.js')}"></script>
        <script src="${request.static_url('clusterflunk:static/js/libs/handlebars.js')}"></script>

        <!-- The Frontend -->
        <script src="${request.static_url('clusterflunk:static/js/index.js')}"></script>

        <!-- Modules -->
        <script src="${request.static_url('clusterflunk:static/js/modules/auth.js')}"></script>
    </head>
    <body>
        <!-- Auth -->
        <script id="login_template" type="template">
            <%include file="auth/login.hbs"/>
        </script>

        <!-- Layouts -->
        <script id="landing_layout" type="layout">
            <%include file="layouts/landing.hbs"/>
        </script>
    </body>
</html>