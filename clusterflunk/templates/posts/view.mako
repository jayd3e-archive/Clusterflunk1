<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>
<%namespace name="children" file="children.mako"/>

<%def name="page()">
    <script id="reply" type="handlebars-template">
        <div class="reply">
            <form id="reply_form" method="POST" action="">
                <input id="post_id" name="post_id" type="hidden" value="{{post_id}}"/>
                <input id="parent_id" name="parent_id" type="hidden" value="{{parent_id}}"/>
                <textarea id="body" name="body"></textarea>
                <input id="submit" name="submit" type="submit"/>
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

    <div class="body_main centered">
        <div class="main_heading">
            <h1>${post.title}</h1>
        </div>
        <div class="post" id="post_${post.id}_">
            ${post.history[latest_rev].description}
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
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>