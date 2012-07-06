<%namespace name="comments" file="../comments/comment.mako"/>
<%inherit file="../layouts/post_base.mako"/>

<%def name="page()">
    <%
        import random
    %>
    <div class="post_view">
        <div class="content">
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
            <div class="title">
                <img class="thumbnail" src="/static/img/thumbnail.png" />
                <a href="/posts/1">${ ' '.join(title_list[:random.randint(4, t_length)]) }</a>
            </div>
            <small><a href="/profile">jayd3e</a> into <a href="/groups/1">Group</a></small>
            <div class="description">
                <span>${ ' '.join(description_list[:random.randint(20, d_length)]) }</span>
            </div>
            <div class="comments">
                % for i in range(random.randint(2, 4)):
                    <%
                        tier = 1
                    %>
                    <div id="solution_${i}" class="comment">
                        <div class="body">
                            <img class="thumbnail" src="/static/img/thumbnail.png" />
                            <a href="/profile">jayd3e:</a>
                            <span>${ ' '.join(comment_list[:random.randint(4, c_length)]) }</span>
                            <small> - ${ str(random.randint(2, 4)) } days ago</small>
                            <div class="clear"></div>
                        </div>
                        <div class="sub_comments">
                            % for i in range(random.randint(1, 3)):
                                ${ comments.comment(comment_list, c_length, tier + 1) }
                            % endfor
                        </div>
                    </div>
                % endfor
            </div>
        </div>
        <aside>
            <div class="group">
                <div class="users">
                <!--
                % for i in range(3, random.randint(7, 10)):
                    --><img class="thumbnail" src="/static/img/thumbnail.png" /><!--
                % endfor
                -->
                </div>
                <a class="title" href="/groups/1">${ ' '.join(title_list[:random.randint(4, t_length)]) }</a>
                <small style="display: block;">286 members - updated 2 minutes ago</small>
                <div class="follow">
                    follow
                </div>
            </div>
        </aside>
    </div>
</%def>