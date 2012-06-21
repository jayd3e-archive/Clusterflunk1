<%inherit file="../layouts/base.mako"/>
<%namespace name="condensed_group" file="condensed_group.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>
<%namespace name="group_toggle" file="../aside/group_toggle.mako"/>

<%def name="page()">
    <div class="add_post">
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <div class="up_arrow"></div>
        <div class="action_area">
            <ul class="horiz-list">
                <li>
                    <a href="#">add group</a>
                </li>
                <li>
                    |
                </li>
                <li>
                    <a href="#">search</a>
                </li>
            </ul>
        </div>
        <div class="sort_area">
            <ul class="horiz-list">
                <li>
                    sort by:
                </li>
                <li>
                    <a href="#">all</a>
                </li>
                <li>
                    |
                </li>
                <li>
                    <a href="#">mine</a>
                </li>
            </ul>
        </div>
    </div>
    <div class="condensed_groups">
        % for i in range(25):
            ${ condensed_group.condensed_group(i) }
        % endfor
    </div>
</%def>

<%def name="aside()">
    ${ group_toggle.group_toggle() }
    ${ watchlist.watchlist() }
</%def>
