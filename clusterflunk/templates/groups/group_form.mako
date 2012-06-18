<%namespace name="group_user_picker" file="../utils/group_user_picker.mako" />

<%def name="group_form()">
    <form class="basic realistic" action="" method="POST">
        <div class="error"></div>
        <input type="text" class="heading" autocomplete="off" value="Group Name" />
        <small>
            created by
            <a href="/profile/jayd3e">jayd3e</a>
            right now
        </small>
        <textarea autocomplete="off">Description</textarea>
        ${ group_user_picker.group_user_picker() }
        <button class="dark">submit</button>
    </form>
</%def>