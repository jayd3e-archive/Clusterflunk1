<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <script id="chosen_user_template" type="handlebars-template">
        <input type="hidden" name="invites" value="{{id}}"/>
        {{ username }}
    </script>

    <script id="available_user_template" type="handlebars-template">
        {{ username }}
    </script>

    <div id="group_create">
        <form class="basic" action="" method="POST">
            <div class="error"></div>
            ${ group_create_form.name(class_="name", autocomplete="off") }
            <ul id="page_actions">
                <li>
                    <a class="primary" href="/posts/create">Create Post</a>
                </li>
            </ul>
            <span class="metadata">
                created by
                <a href="/profile/${user.username}">${user.username}</a>
                right now
            </span>
            ${ group_create_form.description(class_="description", autocomplete="off") }
            <ul class="chosens">
                <li>
                    <input class="choose_input" type="text" name="user" autocomplete="off"/>
                </li>
            </ul>
            <ul class="availables">
            </ul>
            <button class="dark" id="create_submit">submit</button>
        </form>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>