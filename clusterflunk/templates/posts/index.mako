<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <div id="post_index">
        <h1>HW</h1>
        <ul id="page_actions">
            <li>
                <a class="primary" href="/posts/create">Create Post</a>
            </li>
        </ul>
        <div class="posts">
            % for post in posts:
                <%
                    latest_rev = len(post.history) - 1
                %>
                <div class="post">
                    <img class="thumbnail" src="/static/img/thumbnail.png"/>
                    <a class="post_name" href="/posts/${post.id}">${post.history[latest_rev].name}</a>
                    <span class="metadata">
                        created in
                        <a href="/groups/${post.study_group.id}">${post.study_group.name}</a>
                        by
                        <a href="/profile/${post.founder.username}">${post.founder.username}</a>
                        ${post.created_timedelta}
                    </span>
                </div>
            % endfor
        </div>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>