<%inherit file="../layouts/base.mako"/>
<%namespace name="condensed_post" file="condensed_post.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div class="page_heading">
        <h1>HW</h1>
        <ul class="page_actions">
            <li><a class="primary" href="/posts/create">Create Post</a></li>
        </ul>
    </div>
    <div class="condensed_posts">
        ${ condensed_post.condensed_post() }
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>