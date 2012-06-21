<%namespace name="group_user_picker" file="../utils/group_user_picker.mako" />

<%def name="status_form()">
    <form class="basic status_form" method="POST" action="">
        <div class="up_arrow"></div>
        <div class="error"></div>
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <textarea name="status">Ask something crazy!</textarea>
        <!--${ group_user_picker.group_user_picker() }-->
    </form>
</%def>
