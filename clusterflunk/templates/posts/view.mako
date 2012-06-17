<%inherit file="../layouts/base.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>
<%namespace name="post_comment" file="../comments/post_comment.mako"/>

<%def name="page()">
    <div id="post_view">
        <h1>Post Name</h1>
        <span class="metadata">
            created in
            <a href="/groups/1">Group Name</a>
            by
            <a href="/profile/jayd3e">jayd3e</a>
            1 day ago
        </span>
        <div class="post" id="post_1">
            <span>This is a post description.</span>
            <ul class="actions">
                <li>
                    <a class="add_comment">add comment</a>
                </li>
            </ul>
        </div>
        <div class="post_comment_tree">
            ${ post_comment.post_comment() }
        </div>
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>