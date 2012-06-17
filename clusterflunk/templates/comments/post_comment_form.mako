<%def name="post_comment_form()">
    <div class="post_comment_form">
        <form class="basic" method="POST" action="">
            <input name="post_id" type="hidden" value="{{post_id}}"/>
            <input name="parent_id" type="hidden" value="{{parent_id}}"/>
            <textarea name="body"></textarea>
            <button class="dark" name="submit">submit</button>
        </form>
    </div>
</%def>