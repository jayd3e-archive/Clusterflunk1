<%inherit file="../layouts/base.mako"/>

<%def name="page()">
    <%
        import random
    %>
    <div class="posts">
        <%
            description = "This is a description that is likely to be the most epic description known to man.You could go 1,000 years and never see another description of this magnitude.  Really, try it some time.  I now that I\'m right, bitch."
            title = "This is a title that can be both very long and very short."
            comment = "This is a variable length comment that can be a number of different lengths depending on how crazy python depends on being.  This comment just helped tons of people."
            description_list = description.split(' ')
            title_list = title.split(' ');
            comment_list = comment.split(' ');
            d_length = len(description_list)
            t_length = len(title_list)
            c_length = len(comment_list)
        %>
        % for i in range(25):
        <div class="post">
            <a class="title" href="#">${ ' '.join(title_list[:random.randint(4, t_length)]) }</a>
            <div class="description">
                <span>${ ' '.join(description_list[:random.randint(20, d_length)]) }</span>
            </div>
            <div class="user_area">
                <img class="thumbnail" src="/static/img/thumbnail.png" />
                <span><a href="/profile">jayd3e</a> into <a href="/group">Group</a></span>
            </div>
            <div class="comments">
                % for i in range(random.randint(1, 5)):
                    <div class="comment">
                        <img class="thumbnail" src="/static/img/thumbnail.png" />
                        <a href="/profile">jayd3e:</a>
                        <span>${ ' '.join(comment_list[:random.randint(4, c_length)]) }</span>
                        <div class="clear"></div>
                    </div>
                % endfor
            </div>
        </div>
        % endfor
    </div>
</%def>