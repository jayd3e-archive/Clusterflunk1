<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <div id="group_view">
        <h1>${group.name}</h1>
        <ul id="page_actions">
            % if group.id in subscribed_group_ids:
                <li>
                    <a class="primary" href="/posts/create?study_group=${group.id}">Create Post</a>
                </li>
            % endif
        </ul>
        <span class="metadata">
            created by
            <a href="/profile/${group.founder.username}">${group.founder.username}</a>
            ${group.created_timedelta}
        </span>
        <div class="group" id="group_${group.id}">
            <span>${group.description}</span>
        </div>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>