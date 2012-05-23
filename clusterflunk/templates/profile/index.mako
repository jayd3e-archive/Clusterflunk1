<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <div class="profile_pic">
        <img src="${request.static_url('clusterflunk:static/img/portrait.png')}" />
    </div>
    <div class="settings">
        <h1>${user.username}</h1>
        <div class="networks">
            % for network in user.memberships:
                <div class="network">
                    ${network.name}
                </div>
            % endfor
            <div class="clear"></div>
        </div>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>