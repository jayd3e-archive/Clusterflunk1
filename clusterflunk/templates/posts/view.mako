<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>
<%namespace name="children" file="children.mako"/>

<%def name="page()">
    <script id="post_comment_form" type="handlebars-template">
        <div class="post_comment_form">
            <form class="basic" method="POST" action="">
                <input name="post_id" type="hidden" value="{{post_id}}"/>
                <input name="parent_id" type="hidden" value="{{parent_id}}"/>
                <textarea name="body"></textarea>
                <button class="dark" name="submit">submit</button>
            </form>
        </div>
    </script>

    <script id="post_comment" type="handlebars-template">
        <span>{{body}}</span>
        <ul class="actions">
            <li>
                <a class="add_comment">add comment</a>
            </li>
        </ul>
        <div class="post_comments">
        </div>
    </script>

    <div id="post_view">
        <h1>${post.title}</h1>
        <div class="post" id="post_${post.id}">
            <span>${post.history[latest_rev].description}</span>
            <ul class="actions">
                <li>
                    <a class="add_comment">add comment</a>
                </li>
            </ul>
        </div>
        <div class="post_comment_tree">
            % for comment in post.comments:
                <div class="post_comment" id="post_comment_${post.id}_${comment.id}">
                    <%
                        last_rev = len(comment.history) - 1
                    %>
                    <span>${comment.history[last_rev].body}</span>
                    <ul class="actions">
                        <li>
                            <a class="add_comment">add comment</a>
                        </li>
                    </ul>
                    ${children.children(comment, post.id)}
                </div>
            % endfor
        </div>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>