<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="body()">
    <div class="body_main centered">
        <div class="group_view">
            <h1>${group.name}</h1>
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>