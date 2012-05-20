<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <div class="body_main centered">
        <div class="main_heading">
            <h1>Articles</h1>
        </div>
        <div class="articles">
        % for article in articles:
            <div class="article">
                <a class="dark" href="/articles/${article.id}">Article #${article.id}</a>
            </div>
        % endfor
        </div>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>