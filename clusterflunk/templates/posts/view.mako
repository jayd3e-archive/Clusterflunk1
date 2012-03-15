<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>
<%namespace name="children" file="children.mako"/>

<%def name="body()">
    <div class="body_main centered">
        <h1 class="blue">${post.title}</h1>
        <div class="post">
            ${post.history[latest_rev].description}
        </div>
        <div class="comments">
            % for comment in post.comments:
                <div class="comment">
                    <%
                        last_rev = len(comment.history) - 1
                    %>
                    ${comment.history[last_rev].body}
                    ${children.children(comment)}
                </div>
            % endfor
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>