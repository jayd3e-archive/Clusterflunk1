<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>
<%namespace name="children" file="children.mako"/>

<%def name="page()">
    <script id="reply" type="handlebars-template">
        <div class="reply">
            <form class="basic" id="reply_form" method="POST" action="">
                <input id="post_id" name="post_id" type="hidden" value="{{post_id}}"/>
                <input id="parent_id" name="parent_id" type="hidden" value="{{parent_id}}"/>
                <textarea id="body" name="body"></textarea>
                <input class="dark" id="submit" name="submit" type="submit"/>
            </form>
        </div>
    </script>

    <script id="comment" type="handlebars-template">
        <div class="child" id="child_{{post_id}}_{{id}}">
            {{body}}
            <div class="post_actions">
                <ul>
                    <li>
                        <a class="add_reply">add comment</a>
                    </li>
                </ul>
            </div>
            <div class="children">
            </div>
        </div>
    </script>

    <div id="post_view">
        <h1>${post.title}</h1>
        <div class="post" id="post_${post.id}_">
            <span>${post.history[latest_rev].description}</span>
            <div class="post_actions">
                <ul>
                    <li>
                        <a class="add_reply">add comment</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="comments">
            % for comment in post.comments:
                <div class="comment" id="comment_${post.id}_${comment.id}">
                    <%
                        last_rev = len(comment.history) - 1
                    %>
                    <span>${comment.history[last_rev].body}</span>
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

<%def name="aside()">
    ${util_side.due()}
</%def>