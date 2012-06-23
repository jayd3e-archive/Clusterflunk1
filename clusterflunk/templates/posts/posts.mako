<%inherit file="../layouts/base.mako"/>
<%namespace name="condensed_post" file="condensed_post.mako"/>
<%namespace name="fav_tags" file="../aside/fav_tags.mako"/>
<%namespace name="group_toggle" file="../aside/group_toggle.mako"/>

<%def name="page()">
    <div class="add_post">
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <div class="up_arrow"></div>
        <div class="action_area">
            <ul class="horiz-list">
                <li>
                    <a href="#">add post</a>
                </li>
            </ul>
        </div>
        <div class="sort_area">
            <ul class="horiz-list">
                <li>
                    sort by:
                </li>
                <li>
                    <a class="active" href="#">new</a>
                </li>
                <li>
                    |
                </li>
                <li>
                    <a href="#">activity</a>
                </li>
                <li>
                    |
                </li>
                <li>
                    <a href="#">followed</a>
                </li>
                <li>
                    |
                </li>
                <li>
                    <a href="#">due</a>
                </li>
            </ul>
        </div>
    </div>
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
    ${ fav_tags.fav_tags() }
</%def>