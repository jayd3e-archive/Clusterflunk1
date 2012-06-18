<%inherit file="../layouts/base.mako"/>
<%namespace name="condensed_group" file="condensed_group.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div class="page_heading">
        <h1>Groups</h1>
        <ul class="page_actions">
            <li>
                <a class="primary" href="/groups/create">Create Group</a>
            </li>
        </ul>
    </div>
    <ul class="categories">
        <li>
            <a href="/groups?category=all">all</a>
        </li>
        <li>|</li>
        <li>
            <a href="/groups?category=mine">mine</a>
        </li>
    </ul>
    <div class="condensed_groups">
        ${ condensed_group.condensed_group() }
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>
