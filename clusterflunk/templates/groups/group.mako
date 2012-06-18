<%inherit file="../layouts/base.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div class="page_heading">
        <h1>Group Name</h1>
        <ul class="page_actions">
            <li>
                <a class="primary" href="/groups/create?study_group=1">Create Group</a>
            </li>
        </ul>
    </div>
    <small>
        created by
        <a href="/profile/jayd3e">jayd3e</a>
        2 days ago
    </small>
    <div class="description">This is a group description.</div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>