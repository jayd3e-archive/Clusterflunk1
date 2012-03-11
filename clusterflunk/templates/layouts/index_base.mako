<%namespace name="header" file="index_header.mako"/>
<!-- base.mako --> 
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" type="text/css" href="/static/css/reset.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/type.css" />
    </head>
    <body>
        <div class="index_header">
            ${header.header(here)}
        </div>
        <div class="index_body">
            ${self.body()}
        </div>
    </body>
</html>