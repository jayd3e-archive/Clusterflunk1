<%namespace name="post_comment_form" file="post_comment_form.mako" />

<%def name="post_comment()">
    <div class="post_comment" id="post_comment_1_1">
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <div class="content">
            <div class="author">
                <a href="/profile/jayd3e">jayd3e</a>
                <span class="metadata">2 days ago</span>
            </div>
            <span>This is a post comment.</span>
            <ul class="actions">
                <li>
                    <a class="add_comment">add comment</a>
                </li>
            </ul>
            ${ post_comment_form.post_comment_form() }
            <div class="post_comments">
            </div>
        </div>
    </div>
</%def>