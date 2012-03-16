<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="body()">
    <div class="body_main centered">
        <%
            last_rev = len(article.history) - 1
        %>
        <h1>${article.history[last_rev].title}</h1>
        <div class="article">
            ${article.history[last_rev].body}
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>