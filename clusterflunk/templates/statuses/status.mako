<%namespace name="status_comment_form" file="status_comment_form.mako" />
<%namespace name="status_comment" file="status_comment.mako"/>

<%def name="status()">
    <div class="status">
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <div class="content">
            <div class="author">
                <a href="/profile/jayd3e">jayd3e</a>
                <small>1 day ago</small>
            </div>
            <span>This is a question.</span>
            <ul class="actions">
                <li>
                    <a class="add_comment">add comment</a>
                </li>
            </ul>
            ${ status_comment_form.status_comment_form() }
            <div class="status_comments">
                ${ status_comment.status_comment() }
            </div>
        </div>
    </div>
</%def>
