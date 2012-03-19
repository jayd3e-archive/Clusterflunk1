<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>
<%namespace name="children" file="children.mako"/>

<%def name="body()">
    <script id="reply" type="handlebars-template">
        <div class="reply">
            <textarea name="added_reply"></textarea>
            <input name="submit" type="submit"/>
        </div>
    </script>

    <div class="body_main centered">
        <h1 class="blue">${post.title}</h1>
        <div class="post">
            ${post.history[latest_rev].description}
        </div>
        <div class="post_actions">
            <ul>
                <li>
                    <a class="add_reply">add comment</a>
                </li>
            </ul>
        </div>
        <div class="comments">
            % for comment in post.comments:
                <div class="comment">
                    <%
                        last_rev = len(comment.history) - 1
                    %>
                    ${comment.history[last_rev].body}
                    <div class="post_actions">
                        <ul>
                            <li>
                                <a class="add_reply">add comment</a>
                            </li>
                        </ul>
                    </div>
                    ${children.children(comment)}
                </div>
            % endfor
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>