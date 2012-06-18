<%namespace name="group_user_picker" file="../utils/group_user_picker.mako" />

<%def name="group_form()">
    <form class="basic" action="" method="POST">
        <div class="error"></div>
        <input type="text" class="name" autocomplete="off" value="Group Name" />
        <ul class="page_actions">
            <li>
                <a class="primary" href="/posts/create">Create Post</a>
            </li>
        </ul>
        <span class="metadata">
            created by
            <a href="/profile/jayd3e">jayd3e</a>
            right now
        </span>
        <textarea class="description" autocomplete="off">Description</textarea>
        ${ group_user_picker.group_user_picker() }
        <button class="dark create_submit">submit</button>
    </form>
</%def>