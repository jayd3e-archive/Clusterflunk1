<%inherit file="../layouts/base.mako"/>
<%namespace name="condensed_post" file="condensed_post.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div class="post_index">
        <h1>HW</h1>
        <ul class="page_actions">
            <li>
                <a class="primary" href="/posts/create">Create Post</a>
            </li>
        </ul>
        <div class="posts">
            ${ condensed_post.condensed_post() }
        </div>
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>