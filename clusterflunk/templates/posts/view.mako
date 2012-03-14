<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="body()">
    <div class="body_main centered">
        <h1 class="blue">${post.title}</h1>
        <div class="post_body">
            ${post.history[latest_rev].description}
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>