<%def name="followed()">
    <div class="followed">
        <h6>followed users</h6>
        % for i in range(4):
            <div class="follow">
                <img class="thumbnail" src="/static/img/thumbnail.png"/>
                <a href="#">jayd3e</a>
            </div>
        % endfor
    </div>
</%def>