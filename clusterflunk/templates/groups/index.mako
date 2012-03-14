<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="body()">
    <div class="body_main centered">
        <h1>Groups</h1>
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
                        <button class="button-small-negative">unsubscribe</button>
                    % else:
                        <button class="button-small-positive">subscribe</button> 
                    % endif
                </div>
            % endfor
            <div class="clear"></div>
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>