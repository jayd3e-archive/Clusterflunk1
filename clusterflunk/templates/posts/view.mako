<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>
<%namespace name="children" file="children.mako"/>

<%def name="body()">
    <script id="reply" type="handlebars-template">
        <div class="reply">
            <form id="reply_form" method="POST" action="">
                <input id="post_id" name="post_id" type="hidden" value="{{post_id}}"/>
                <input id="parent_id" name="parent_id" type="hidden" value="{{parent_id}}"/>
                <textarea id="reply" name="reply"></textarea>
                <input id="submit" name="submit" type="submit"/>
            </form>
        </div>
    </script>

    <div class="body_main centered">
        <h1 class="blue">${post.title}</h1>
        <div class="post" id="post_${post.id}_">
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
                <div class="comment" id="comment_${post.id}_${comment.id}">
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
                    ${children.children(comment, post.id)}
                </div>
            % endfor
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>