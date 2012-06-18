<%inherit file="layouts/base.mako"/>
<%namespace name="status" file="statuses/status.mako"/>
<%namespace name="status_form" file="statuses/status_form.mako"/>
<%namespace name="watchlist" file="aside/watchlist.mako"/>

<%def name="page()">
    <div class="page_heading">
        <h1>Feed</h1>
    </div>
    ${ status_form.status_form() }
    <div class="statuses">
        ${ status.status() }
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>