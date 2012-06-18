<%inherit file="../layouts/base.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div class="profile">
        <div class="profile_pic">
            <img src="/static/img/portrait.png" />
        </div>
        <div class="settings">
            <h1>jayd3e</h1>
            <ul class="networks">
                <li class="network">
                    <span>University of Iowa</span>
                </li>
            </ul>
        </div>
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>