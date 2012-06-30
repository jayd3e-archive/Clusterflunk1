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
            <header class="header post_header">
                ${ header.header(here) }
            </header>
        </div>
        <div class="page" style="padding: 0px 15px;">
            ${ self.page() }
        </div>
    </body>
</html>