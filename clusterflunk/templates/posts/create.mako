<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <div id="post_create">
        <form class="basic" action="" method="POST">
            <div class="error"></div>
            ${post_create_form.name(class_="name", autocomplete="off")}
            <span class="metadata">
                created in
                ${post_create_form.study_group(class_="study_group", autocomplete="off")}
                by
                <a href="/profile/${user.username}">${user.username}</a>
                right now
            </span>
            ${post_create_form.description(class_="description", autocomplete="off")}
            <button class="dark" id="create_submit">submit</button>
        </form>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>