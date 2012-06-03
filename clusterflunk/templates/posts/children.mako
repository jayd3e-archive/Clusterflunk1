<%def name="children(comment, post_id)">
    <div class="post_comments">
        % if comment.replies:
            % for child in comment.replies:
                <div class="post_comment" id="post_comment_${post_id}_${child.id}">
                    <%
                        last_rev = len(comment.history) - 1
                        child_rev = child.history[last_rev]
                    %>
                    <div class="author">
                        <a href="/profile/${child_rev.author.username}">${child_rev.author.username}</a>
                        <span class="metadata">${child_rev.created_timedelta}</span>
                    </div>
                    <span>${child_rev.body}</span>
                    <ul class="actions">
                        <li>
                            <a class="add_comment">add comment</a>
                        </li>
                    </ul>
                    ${children(child, post_id)}
                </div>
            % endfor
        % endif
    </div>
</%def>