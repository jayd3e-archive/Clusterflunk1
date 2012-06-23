<%def name="condensed_group(num)">
        % if (num % 2) == 0:
            <div class="condensed_group">
        % else:
            <div class="condensed_group odd">
        % endif
        <div class="thumbnails">
            <img class="thumbnail" src="/static/img/thumbnail.png"/>
            <img class="thumbnail" src="/static/img/thumbnail.png"/>
            <img class="thumbnail" src="/static/img/thumbnail.png"/>
        </div>
        <div class="up_arrow"></div>
        <div class="white_area">
            <div class="content">
                <a href="/groups/1">Group Name</a>
                <small>
                    created by
                    <a href="/profile/jayd3e">jayd3e</a>
                    2 days ago
                </small>
            </div>
            <div class="buttons">
                <a href="#">
                    subscribe
                </a>
            </div>
        </div>
    </div>
</%def>
