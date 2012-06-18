<%namespace name="group_user_picker" file="../utils/group_user_picker.mako" />

<%def name="status_form()">
    <form class="basic status_form" method="POST" action="">
        <div class="error"></div>
        <textarea class="status" name="status">Ask something crazy!</textarea>
        ${ group_user_picker.group_user_picker() }
        <button class="dark status_submit">submit</button>
    </form>
</%def>
