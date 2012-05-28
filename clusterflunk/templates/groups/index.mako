<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <div id="group_index">
        <h1>Groups</h1>
        <ul id="page_actions">
            <li>
                <a class="primary" href="/groups/create">Create</a>
            </li>
        </ul>
        <ul id="categories" class="horiz-list">
            <li>
                <a href="/groups?category=all">all</a>
            </li>
            <li>|</li>
            <li>
                <a href="/groups?category=mine">mine</a>
            </li>
        </ul>
        <div id="groups">
            % for group in groups:
                <div class="group" id="group_${group.id}">
                    <a class="group_name" href="/groups/${group.id}">${group.name}</a>
                    % if group in user.subscribed_groups:
                        <button class="dark">
                            unsubscribe
                        </button>
                    % else:
                        <button class="primary">
                            subscribe
                        </button>
                    % endif
                </div>
            % endfor
        </div>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>