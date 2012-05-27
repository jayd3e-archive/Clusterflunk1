<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="page()">
    <script id="invite_template" type="handlebars-template">
        <li>
            <input type="hidden" name="invites" value="{{id}}"/>
            {{label}}
        </li>
    </script>

    <div id="group_create">
        <h1>Create a Group</h1>
        <form class="basic" action="" method="POST">
            ${ group_create_form.name(class_="group_name") }
            ${ group_create_form.description(class_="group_description") }
            <ul class="invites">
                <li id="invites_input">
                    <input id="invite_input" type="text" name="invite"/>
                </li>
            </ul>
            <input class="dark" id="create_group_submit" name="submit" type="submit" />
        </form>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>