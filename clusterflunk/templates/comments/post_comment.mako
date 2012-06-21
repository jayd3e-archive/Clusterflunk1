<%namespace name="post_comment_form" file="post_comment_form.mako" />

<%def name="post_comment(num=0)">
    <div class="post_comment">
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <div class="up_arrow"></div>
        <div class="white_area">
            <div class="content">
                <div class="author">
                    <a href="/profile/jayd3e">jayd3e</a>
                    <small>2 days ago</small>
                </div>
                <span>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span>
                <ul class="actions">
                    <li>
                        <a class="add_comment">add comment</a>
                    </li>
                </ul>
                <!--${ post_comment_form.post_comment_form() }-->
            </div>
        </div>
        <div style="clear: both;"></div>
        <div class="post_comments">
            % if num != 4:
                ${post_comment(num + 1)}
            % endif
        </div>
    </div>
</%def>