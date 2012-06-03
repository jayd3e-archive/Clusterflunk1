<%inherit file="layouts/base.mako"/>
<%namespace name="util_side" file="utilities/side.mako"/>

<%def name="page()">
    <script id="status_template" type="handlebars-template">
        <div class="author">
            <a href="/profile/{{username}}">{{ username }}</a>
            <span class="metadata">{{ created_timedelta }}</span>
        </div>
        <span>{{ body }}</span>
        <ul class="actions">
            <li>
                <a class="add_comment">add comment</a>
            </li>
        </ul>
        <div class="status_comments"></div>
    </script>

    <script id="chosen_group_template" type="handlebars-template">
        {{ name }}
    </script>

    <script id="available_group_template" type="handlebars-template">
        {{ name }}
    </script>

    <script id="status_comment_form_template" type="handlebars-template">
        <div class="status_comment_form">
            <form class="basic" method="POST" action="">
                <input name="status_id" type="hidden" value="{{status_id}}"/>
                <textarea name="body"></textarea>
                <button class="dark" name="submit">submit</button>
            </form>
        </div>
    </script>

    <script id="status_comment_template" type="handlebars-template">
        <span>{{ body }}</span>
        <a href="/profile/{{ username }}">{{ username }}</a>
        <span class="metadata">{{ created_timedelta }}</span>
    </script>

    <div id="feed">
        <h1>Feed</h1>
        <form class="basic" id="status_form" method="POST" action="" autocomplete="off">
            <div class="error"></div>
            <textarea id="status" name="status">Ask something crazy!</textarea>
            <ul class="chosens">
                <li>
                    <input class="choose_input" type="text" name="group"/>
                </li>
            </ul>
            <ul class="availables">
            </ul>
            <button class="dark" id="status_submit">submit</button>
        </form>
        <div id="statuses">
            % for status in statuses:
                <div class="status" id="status_${status.id}">
                    <%
                        last_status_rev = len(status.history) - 1
                        status_rev = status.history[last_status_rev]
                    %>
                    <div class="author">
                        <a href="/profile/${status_rev.author.username}">${status_rev.author.username}</a>
                        <span class="metadata">${status_rev.created_timedelta}</span>
                    </div>
                    <span>${status_rev.body}</span>
                    <ul class="actions">
                        <li>
                            <a class="add_comment">add comment</a>
                        </li>
                    </ul>
                    <div class="status_comments">
                        % for comment in status.comments:
                            <div class="status_comment" id="status_comment_${status.id}_${comment.id}">
                                <%
                                    last_comment_rev = len(comment.history) - 1
                                    comment_rev = comment.history[last_comment_rev]
                                %>
                                <span>${comment_rev.body}</span> -
                                <a href="/profile/${comment_rev.author.username}">${comment_rev.author.username}</a>
                                <span class="metadata">${comment_rev.created_timedelta}</span>
                            </div>
                        % endfor
                    </div>
                </div>
            % endfor
        </div>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>