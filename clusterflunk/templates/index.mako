<%inherit file="layouts/base.mako"/>
<%namespace name="util_side" file="utilities/side.mako"/>

<%def name="body()">
    <div class="body_main centered">
        <h1>HW</h1>
        <div class="posts">
            % for post in posts:
                <%
                    latest_rev = len(post.history) - 1
                %>
                <div class="post">
                    <a class="dark" href="/posts/${post.id}">${post.history[latest_rev].name}</a>
                </div>
            % endfor
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>