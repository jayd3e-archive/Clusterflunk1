<%def name="comment(comment_list, c_length, tier)">
    <%
        import random
    %>
    <div class="comment">
        <div class="body">
            <img class="thumbnail" src="/static/img/thumbnail.png" />
            <a href="/profile">jayd3e:</a>
            <span>${ ' '.join(comment_list[:random.randint(4, c_length)]) }</span>
            <small> - ${ str(random.randint(2, 4)) } days ago</small>
            <div class="clear"></div>
        </div>
        <div class="sub_comments">
            % if tier < 4:
                % for i in range(random.randint(1, 3)):
                    ${ comment(comment_list, c_length, tier + 1)}
                % endfor
            % endif
            <div class="clear"></div>
        </div>
    </div>
</%def>