<%inherit file="../layouts/base.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div style="background-color: #FFF; padding: 5px 10px 10px 10px; border-radius: 3px;">
        <div class="page_heading">
            <h1 style="font-size: 20px;">Group Name</h1>
        </div>
        <small>
            created in
            <a href="/groups/1">Group Name</a>
            by
            <a href="/profile/jayd3e">jayd3e</a>
            1 day ago
        </small>
        <div class="description">This is a group description.</div>
        <ul class="actions">
            <li>
                <a class="add_comment">add comment</a>
            </li>
        </ul>
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>