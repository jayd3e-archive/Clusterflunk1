<%inherit file="../layouts/base.mako"/>
<%namespace name="util_side" file="../utilities/side.mako"/>

<%def name="body()">
    <script id="invite_template" type="handlebars-template">
        <li class="invite">
            <input type="hidden" name="invites" value="{{id}}"/>
            {{label}}
        </li>
    </script>

    <div class="body_main centered">
        <div class="main_heading">
            <h1>Create a Group</h1>
        </div>
        <div class="create_group">
            <form class="create_group_form" action="" method="POST">
                ${ group_create_form.name(class_="group_name") }
                ${ group_create_form.description(class_="group_description") }
                <div class="invites_container">
                    <ul class="invites">
                        <li class="invites_input" id="invites_input">
                            <input id="invite_input" type="text" name="invite"/>
                        </li>
                        <div class="clear"></div>
                    </ul>
                    <div class="clear"></div>
                </div>
                <input id="create_group_submit" name="submit" type="submit" />
            </form>
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>