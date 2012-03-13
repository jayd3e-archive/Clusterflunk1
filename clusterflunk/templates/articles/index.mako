<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="body()">
    <div class="body_main centered">
        <h1>Articles</h1>
        <div class="articles">
        % for article in articles:
            <div class="article">
                <a class="dark" href="/article/${article.id}">Article #${article.id}</a>
            </div>
        % endfor
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>