<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>
<%namespace name="children" file="children.mako"/>

<%def name="page()">
    <script id="post_comment_form_template" type="handlebars-template">
        <div class="post_comment_form">
            <form class="basic" method="POST" action="">
                <input name="post_id" type="hidden" value="{{post_id}}"/>
                <input name="parent_id" type="hidden" value="{{parent_id}}"/>
                <textarea name="body"></textarea>
                <button class="dark" name="submit">submit</button>
            </form>
        </div>
    </script>

    <script id="post_comment_template" type="handlebars-template">
        <div class="author">
            <a href="/profile/{{ username }}">{{ username }}</a>
            <span class="metadata">{{ created_timedelta }}</span>
        </div>
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
        <%
            last_rev = len(post.history) - 1
            post_rev = post.history[last_rev]
        %>
        <h1>${post_rev.name}</h1>
        <span class="metadata">
            created in
            <a href="/group/${post.study_group.id}">${post.study_group.name}</a>
            by
            <a href="/profile/${post_rev.author.username}">${post_rev.author.username}</a>
            ${post.created_timedelta}
        </span>
        <div class="post" id="post_${post.id}">
            <span>${post_rev.description}</span>
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
                        comment_rev = comment.history[last_rev]
                    %>
                    <div class="author">
                        <a href="/profile/${comment_rev.author.username}">${comment_rev.author.username}</a>
                        <span class="metadata">${comment_rev.created_timedelta}</span>
                    </div>
                    <span>${comment_rev.body}</span>
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