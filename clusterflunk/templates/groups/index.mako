<%inherit file="../layouts/base.mako"/>
<%namespace name="condensed_group" file="condensed_group.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div class="group_index">
        <h1>Groups</h1>
        <ul class="page_actions">
            <li>
                <a class="primary" href="/groups/create">Create Group</a>
            </li>
        </ul>
        <ul class="horiz-list categories">
            <li>
                <a href="/groups?category=all">all</a>
            </li>
            <li>|</li>
            <li>
                <a href="/groups?category=mine">mine</a>
            </li>
        </ul>
        <div class="groups">
            ${ condensed_group.condensed_group() }
        </div>
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>