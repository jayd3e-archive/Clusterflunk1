<%inherit file="../layouts/base.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>
<%namespace name="post_comment" file="../comments/post_comment.mako"/>

<%def name="page()">
    <div class="page_heading">
        <h1>Post Name</h1>
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
    <div class="post_comment_tree">
        ${ post_comment.post_comment() }
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>