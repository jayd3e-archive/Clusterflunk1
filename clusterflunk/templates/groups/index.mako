<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <div class="body_main centered">
        <div class="main_heading">
            <h1>Groups</h1>
        </div>
        <ul>
            <a class="create_group_link" href="/groups/create">
                <div id="create_group" class="button button-small-positive">create</div>
            </a>
        </ul>
        <div class="categories">
            <ul>
                <li>
                    <a href="/groups?category=all">all</a>
                </li>
                <li>|</li>
                <li>
                    <a href="/groups?category=mine">mine</a>
                </li>
            </ul>
        </div>
        <div class="groups">
            % for group in groups:
                <div class="group">
                    <a href="/groups/${group.id}">${group.name}</a>
                    % if group in user.subscribed_groups:
                        <button id="${group.id}">
                                unsubscribe
                        </button>
                    % else:
                        <button id="${group.id}">
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