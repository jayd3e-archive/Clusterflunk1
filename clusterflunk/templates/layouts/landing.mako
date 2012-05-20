<!-- base.mako --> 
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" type="text/css" href="${request.static_url('clusterflunk:static/slicknasty/css/bootstrap.css')}" />
        <link rel="stylesheet" type="text/css" href="${request.static_url('clusterflunk:static/css/bootstrap.css')}" />
    </head>
    <body>
        <div class="main">
            ${self.page()}
        </div>
    </body>
</html>