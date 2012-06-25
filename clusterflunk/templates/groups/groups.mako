<%inherit file="../layouts/base.mako"/>

<%def name="page()">
    <%
        import random
    %>
    <div class="groups">
        % for i in range(25):
        <div class="group">
            <div class="users">
            % for i in range(3, random.randint(7, 10)):
                <img class="thumbnail" src="/static/img/thumbnail.png" />
            % endfor
            </div>
            <a class="title" href="#">This is a title</a>
            <small style="display: block;">286 members - updated 2 minutes ago</small>
            <div class="follow">
                follow
            </div>
        </div>
        % endfor
    </div>
</%def>