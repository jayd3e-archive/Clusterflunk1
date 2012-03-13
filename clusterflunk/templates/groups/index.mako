<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="body()">
    <div class="body_main centered">
        <h1>Groups</h1>
        <div class="groups">
            % for group in groups:
                <div class="group">
                    <a class="dark" href="/groups/${group.id}">${group.name}</a>
                    <button class="button-small">subscribe</button> 
                </div>
            % endfor
            <div class="clear"></div>
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>