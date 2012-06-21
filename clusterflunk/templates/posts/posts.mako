<%inherit file="../layouts/base.mako"/>
<%namespace name="condensed_post" file="condensed_post.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>
<%namespace name="group_toggle" file="../aside/group_toggle.mako"/>

<%def name="page()">
    <div class="add_post">
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <div class="up_arrow"></div>
        <div class="action_area">
            <ul class="horiz-list">
                <li>
                    <a href="#">add post</a>
                </li>
            </ul>
        </div>
        <div class="sort_area">
            <ul class="horiz-list">
                <li>
                    sort by:
                </li>
                <li>
                    <a href="#">new</a>
                </li>
                <li>
                    |
                </li>
                <li>
                    <a href="#">activity</a>
                </li>
                <li>
                    |
                </li>
                <li>
                    <a href="#">followed</a>
                </li>
            </ul>
        </div>
    </div>
    <div class="condensed_posts">
        % for i in range(10):
        ${ condensed_post.condensed_post() }
        % endfor
    </div>
</%def>

<%def name="aside()">
    ${ group_toggle.group_toggle() }
    ${ watchlist.watchlist() }
</%def>