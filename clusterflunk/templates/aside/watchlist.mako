<%namespace name="condensed_post" file="../posts/condensed_post.mako"/>

<%def name="watchlist()">
    <div class="watchlist">
        <h6>followed posts</h6>
        % for i in range(4):
            <div class="watched">
                <div class="watched_post">
                    <div class="content">
                        <a style="display:block;" href="/posts/1">This Is A Post Name</a>
                        <a href="/groups/1">Group</a> - <a href="/profile/jayd3e">jayd3e</a>
                        <small>
                            Due in: <span class="red">2</span> days <span class="red">3</span> hrs <span class="red">4</span> mins
                        </small>
                    </div>
                </div>
            </div>
        % endfor
    </div>
</%def>