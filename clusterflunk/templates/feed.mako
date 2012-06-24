<%inherit file="layouts/base.mako"/>
<%namespace name="status" file="statuses/status.mako"/>
<%namespace name="status_form" file="statuses/status_form.mako"/>
<%namespace name="watchlist" file="aside/watchlist.mako"/>
<%namespace name="followed" file="aside/followed.mako"/>
<%namespace name="group_toggle" file="aside/group_toggle.mako"/>

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
    ${ status_form.status_form() }
    <div class="statuses">
        % for i in range(5):
        ${ status.status() }
        % endfor
    </div>
</%def>

<%def name="aside()">
    ${ group_toggle.group_toggle() }
</%def>