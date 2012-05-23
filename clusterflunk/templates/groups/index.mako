<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <div class="body_main centered">
        <div class="main_heading float_left">
            <h1>Groups</h1>
        </div>
        <ul class="buttons">
            <a class="create_group_link" href="/groups/create">
                <div id="create_group" class="button button-small-positive">create</div>
            </a>
        </ul>
        <div class="clear"></div>
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
            <div class="clear"></div>
        </div>
        <div class="groups">
            % for group in groups:
                <div class="group">
                    <a class="dark" href="/groups/${group.id}">${group.name}</a>
                    % if group in user.subscribed_groups:
                        <button
                            id="${group.id}" 
                            class="button-small-negative">
                                unsubscribe
                        </button>
                    % else:
                        <button
                            id="${group.id}"
                            class="button-small-positive">
                                subscribe
                        </button> 
                    % endif
                </div>
            % endfor
            <div class="clear"></div>
        </div>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>