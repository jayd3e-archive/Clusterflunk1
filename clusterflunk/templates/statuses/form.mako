<%def name="form()">
    <div class="status_comment_form">
        <form class="basic" method="POST" action="">
            <input name="status_id" type="hidden" value="{{status_id}}"/>
            <textarea name="body"></textarea>
            <button class="dark" name="submit">submit</button>
        </form>
    </div>
</%def>