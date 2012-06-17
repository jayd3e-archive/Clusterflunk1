<%inherit file="../layouts/base.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div class="group_view">
        <h1>Group Name</h1>
        <ul class="page_actions">
            <li>
                <a class="primary" href="/posts/create?study_group=1">Create Post</a>
            </li>
        </ul>
        <span class="metadata">
            created by
            <a href="/profile/jayd3e">jayd3e</a>
            2 days ago
        </span>
        <div class="group">
            <span>This is a group description.</span>
        </div>
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>