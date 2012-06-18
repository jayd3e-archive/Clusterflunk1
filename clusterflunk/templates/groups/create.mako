<%inherit file="../layouts/base.mako"/>
<%namespace name="group_form" file="group_form.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div class="group_create">
        ${ group_form.group_form() }
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>