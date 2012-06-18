<%inherit file="../layouts/base.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>
<%namespace name="post" file="post.mako"/>
<%namespace name="post_comment" file="../comments/post_comment.mako"/>

<%def name="page()">
    <div class="post_view">
        ${ post.post() }
        <div class="post_comment_tree">
            ${ post_comment.post_comment() }
        </div>
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>