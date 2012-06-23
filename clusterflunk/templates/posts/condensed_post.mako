<%def name="condensed_post(odd)">
    <div class="condensed_post ${odd}">
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <div class="up_arrow"></div>
        <div class="white_area">
            <div class="content">
                <a href="/posts/1">This Is A Post Name</a>
                <small>
                    created in
                    <a href="/groups/1">Group</a>
                    by
                    <a href="/profile/jayd3e">jayd3e</a>
                    2 days ago
                </small>
            </div>
            <div class="buttons">
                <a href="#">follow</a>
                <a href="#">edit</a>
                <a href="#">delete</a>
            </div>
        </div>
    </div>
</%def>