<%def name="post_form()">
    <form class="basic" action="" method="POST">
        <div class="error"></div>
        <input type="text" class="name" autocomplete="off" value="Post Name">
        <span class="metadata">
            created in
            <a href="/groups/1">Group</a>
            by
            <a href="/profile/jayd3e">jayd3e</a>
            right now
        </span>
        <textarea class="description" autocomplete="off">Description</textarea>
        <button class="dark create_submit">submit</button>
    </form>
</%def>