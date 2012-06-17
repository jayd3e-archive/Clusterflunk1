<%namespace name="form" file="form.mako"/>

<%def name="status()">
    <div class="status" id="status_1">
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <div class="content">
            <div class="author">
                <a href="/profile/jayd3e">jayd3e</a>
                <span class="metadata">1 day ago</span>
            </div>
            <span>This is a question.</span>
            <ul class="actions">
                <li>
                    <a class="add_comment">add comment</a>
                </li>
            </ul>
            ${ form.form() }
            <div class="status_comments">
                <div class="status_comment" id="status_comment_1_1">
                    <span>This is a comment.</span> -
                    <a href="/profile/jayd3e">jayd3e</a>
                    <span class="metadata">2 days ago</span>
                </div>
            </div>
        </div>
    </div>
</%def>
