<%inherit file="../layouts/base.mako"/>
<%namespace name="post_form" file="post_form.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div class="post_create">
        ${ post_form.post_form() }
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>