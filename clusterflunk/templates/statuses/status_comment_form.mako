<%def name="status_comment_form()">
    <form class="basic status_comment_form" method="POST" action="">
        <input name="status_id" type="hidden" value="{{status_id}}"/>
        <textarea name="body"></textarea>
        <button class="dark" name="submit">submit</button>
    </form>
</%def>