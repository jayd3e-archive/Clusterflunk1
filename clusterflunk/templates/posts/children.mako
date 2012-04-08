<%def name="children(comment, post_id)">
    % if comment.replies:
        <div class="children">
            % for child in comment.replies:
                <div class="child" id="child_${post_id}_${child.id}">
                    <%
                        last_rev = len(comment.history) - 1
                    %>
                    ${child.history[last_rev].body}
                    <div class="post_actions">
                        <ul>
                            <li>
                                <a class="add_reply">add comment</a>
                            </li>
                        </ul>
                    </div>
                    ${children(child, post_id)}
                </div>
            % endfor
        </div>
    % endif
</%def>