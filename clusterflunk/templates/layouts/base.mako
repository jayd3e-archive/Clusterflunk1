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
</html>