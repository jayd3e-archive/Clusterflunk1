<%inherit file="../layouts/base.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>
<%namespace name="post_comment" file="../comments/post_comment.mako"/>
<%namespace name="online" file="../aside/online.mako"/>

<%def name="page()">
    <div style="background-color: #FFF; padding: 5px 10px 10px 10px; border-radius: 3px;">
        <div class="page_heading">
            <h1 style="font-size: 20px;">Post Name</h1>
        </div>
        <small>
            created in
            <a href="/groups/1">Group Name</a>
            by
            <a href="/profile/jayd3e">jayd3e</a>
            1 day ago
        </small>
        <div class="description">This is a post description.</div>
        <ul class="actions">
            <li>
                <a class="add_comment">add comment</a>
            </li>
        </ul>
    </div>
    <div class="post_comment_tree">
        % for i in range(3):
            <% num = 0 %>
            ${ post_comment.post_comment(num) }
        % endfor
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
    ${ online.online() }
</%def>