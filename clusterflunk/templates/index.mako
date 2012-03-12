<%inherit file="layouts/base.mako"/>
<%namespace name="util_side" file="utilities/side.mako"/>

<%def name="body()">
    <div class="body_main centered">
        <h1>HW</h1>
        <div class="posts">
            % for post in posts:
                <%
                up = "up"
                down = "down"
                vote = ""

                for votes in post.votes:
                    if user.id == votes.user_id and post.id == votes.post_id:
                        vote = votes.vote
                        if vote == 1:
                            up = up + " active"
                        elif  vote == -1:
                            down = down + " active"
                        break
                    else:
                        continue
                %>
                <div class="post">
                    <div class="id">Post #${post.id}</div>
                    <div class="vote">
                        <div class="${up}" onClick="javascript: toggle_vote(this, ${user.id}, ${post.id}, 'up');"></div>
                        <div class="${down}" onClick="javascript: toggle_vote(this, ${user.id}, ${post.id}, 'down');"></div>
                    </div>
                    <div class="score">${post.score}</div>
                </div>
            % endfor
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>