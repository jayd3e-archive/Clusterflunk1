<%def name="children(comment, post_id)">
    <div class="post_children">
        % if comment.replies:
            % for child in comment.replies:
                <div class="post_child" id="child_${post_id}_${child.id}">
                    <%
                        last_rev = len(comment.history) - 1
                    %>
                    <span>${child.history[last_rev].body}</span>
                    <ul class="actions">
                        <li>
                            <a class="add_reply">add comment</a>
                        </li>
                    </ul>
                    ${children(child, post_id)}
                </div>
            % endfor
        % endif
    </div>
</%def>