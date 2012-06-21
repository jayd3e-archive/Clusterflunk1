<%namespace name="status_comment_form" file="status_comment_form.mako" />
<%namespace name="status_comment" file="status_comment.mako"/>

<%def name="status()">
    <div class="status">
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <div class="white_area">
            <div class="content">
                <div class="up_arrow"></div>
                <div class="author">
                    <a href="/profile/jayd3e">jayd3e</a>
                    <small>1 day ago</small>
                </div>
                <span>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.</span>
                <ul class="actions">
                    <li>
                        <a class="add_comment">add comment</a>
                    </li>
                </ul>
                <!--${ status_comment_form.status_comment_form() }-->
                <div class="status_comments">
                    % for i in range(5):
                    ${ status_comment.status_comment() }
                    % endfor
                </div>
            </div>
        </div>
    </div>
</%def>
