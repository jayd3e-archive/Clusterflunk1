<%inherit file="../layouts/base.mako"/>

<%def name="page()">
    <%
        import random
    %>
    <div class="posts">
        <%
            description = "This is a description that is likely to be the most epic description known to man.You could go 1,000 years and never see another description of this magnitude.  Really, try it some time.  I now that I\'m right, bitch."
            description_list = description.split(' ')
            d_length = len(description_list)
        %>
        % for i in range(25):
        <div class="post">
            <a class="title" href="#">This is a title</a>
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
                        <span>This is a comment</span>
                    </div>
                % endfor
            </div>
        </div>
        % endfor
    </div>
</%def>