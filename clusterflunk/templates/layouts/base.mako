<%namespace name="header" file="header.mako"/>
<%namespace name="footer" file="footer.mako"/>
<!-- base.mako -->
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.css" />
    </head>
    <body>
        <div class="top">
            <div class="container">
                <header class="header">
                    ${ header.header(here) }
                </header>
            </div>
        </div>
        <div class="main">
            <div class="container">
                <article class="page">
                    ${ self.page() }
                </article>
                <aside class="aside">
                    ${ self.aside() }
                </aside>
            </div>
        </div>
    </body>

    <script type="text/javascript" charset="utf-8" src="/static/js/libs/jquery-1.7.1.js"></script>
    <script type="text/javascript" charset="utf-8" src="/static/js/libs/jquery.tipsy.js"></script>
    <script type="text/javascript" charset="utf-8" src="/static/js/wireframes.js"></script>
</html>