<%def name="post_form()">
    <form class="basic realistic" action="" method="POST">
        <div class="error"></div>
        <input type="text" class="heading" autocomplete="off" value="Post Name">
        <small>
            created in
            <select autocomplete="off" name="study_group">
                <option value="3">Physics 103</option>
                <option value="1">Physics 101</option>
            </select>
            by
            <a href="/profile/jayd3e">jayd3e</a>
            right now
        </small>
        <textarea autocomplete="off">Description</textarea>
        <button class="dark">submit</button>
    </form>
</%def>