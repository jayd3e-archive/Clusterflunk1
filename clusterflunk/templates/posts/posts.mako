<%inherit file="../layouts/base.mako"/>
<%namespace name="condensed_post" file="condensed_post.mako"/>
<%namespace name="fav_tags" file="../aside/fav_tags.mako"/>
<%namespace name="group_toggle" file="../aside/group_toggle.mako"/>

<%def name="subnav()">
    <ul class="horiz-list">
        <li>
            <a href="#">all</a>
        </li>
        <li>
            <a href="#">mine</a>
        </li>
    </ul>
</%def>

<%def name="page()">
    <div class="condensed_posts">
        % for i in range(10):
        <%
            if (i % 2) == 0:
                odd = ""
            else:
                odd = "odd"
        %>
        ${ condensed_post.condensed_post(odd) }
        % endfor
    </div>
</%def>

<%def name="aside()">
    ${ group_toggle.group_toggle() }
</%def>