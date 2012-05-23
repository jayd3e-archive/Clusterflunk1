<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
        <h1>Articles</h1>
        <ul class="articles">
            % for article in articles:
                <li class="article">
                    <a href="/articles/${article.id}">Article #${article.id}</a>
                </li>
            % endfor
        </ul>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>