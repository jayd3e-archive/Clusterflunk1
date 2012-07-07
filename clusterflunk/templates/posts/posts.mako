<%inherit file="../layouts/base.mako"/>

<%def name="page()">
    <div class="posts">
        % for i in range(25):
        <div class="post">
            <a class="title" href="#">This is a title</a>
            <div class="description">
                This is a description of epic proportions.
            </div>
        </div>
        % endfor
    </div>
</%def>