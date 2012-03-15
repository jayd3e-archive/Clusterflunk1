<%def name="children(comment)">
    % if comment.replies:
        <div class="children">
            % for child in comment.replies:
                <div class="child">
                    <%
                        last_rev = len(comment.history) - 1
                    %>
                    ${child.history[last_rev].body}
                    ${children(child)}
                </div>
            % endfor
        </div>
    % endif
</%def>