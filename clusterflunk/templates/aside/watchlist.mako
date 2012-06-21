<%namespace name="condensed_post" file="../posts/condensed_post.mako"/>

<%def name="watchlist()">
    <div class="watchlist">
        % for i in range(4):
            <div class="watched">
                <ul class="timer horiz-list">
                    <li class="num">3<span class="word">days</span></li>
                    <li class="num">4<span class="word">hrs</span></li>
                    <li class="num">35<span class="word">mins</span></li>
                </ul>
                <div class="watched_post">
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
                </div>
            </div>
        % endfor
    </div>
</%def>