<%inherit file="../layouts/base.mako"/>

<%def name="page()">
    <div class="posts">
        % for i in range(25):
        <div class="post">
            <div class="inner"></div>
        </div>
        % endfor
    </div>
</%def>