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
            <ul class="chosens">
                <li>
                    <input class="choose_input" type="text" name="group"/>
                </li>
            </ul>
            <ul class="availables">
            </ul>
            <button class="dark" id="status_submit">submit</button>
        </form>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>