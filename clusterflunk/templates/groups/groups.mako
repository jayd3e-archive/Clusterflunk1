<%inherit file="../layouts/base.mako"/>
<%namespace name="condensed_group" file="condensed_group.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>
<%namespace name="group_toggle" file="../aside/group_toggle.mako"/>

<%def name="subnav()">
    <ul class="horiz-list">
        <li>
            <a href="#">all</a>
        </li>
        <li>
            <a href="#">mine</a>
        </li>
    </ul>
</%def>

<%def name="page()">
    <div class="condensed_groups">
        % for i in range(25):
            ${ condensed_group.condensed_group(i) }
        % endfor
    </div>
</%def>

<%def name="aside()">
    ${ group_toggle.group_toggle() }
</%def>
