<%def name="children(comment)">
    % if comment.replies:
        <div class="children">
            % for child in comment.replies:
                <div class="child">
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
                    ${children(child)}
                </div>
            % endfor
        </div>
    % endif
</%def>