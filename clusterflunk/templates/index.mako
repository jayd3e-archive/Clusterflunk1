<%inherit file="layouts/base.mako"/>
<%namespace name="util_side" file="utilities/side.mako"/>

<%def name="page()">
    <script id="status_template" type="handlebars-template">
        <div class="author">
            <a href="/profile/{{username}}">{{ username }}</a>
        </div>
        <span>{{ body }}</span>
        <ul class="actions">
            <li>
                <a class="add_comment">add comment</a>
            </li>
        </ul>
    </script>

    <script id="chosen_group_template" type="handlebars-template">
        {{ name }}
    </script>

    <script id="available_group_template" type="handlebars-template">
        {{ name }}
    </script>

    <script id="status_comment_form" type="handlebars-template">
        <div class="status_comment_form">
            <form class="basic" method="POST" action="">
                <input name="status_id" type="hidden" value="{{status_id}}"/>
                <textarea name="body"></textarea>
                <button class="dark" name="submit">submit</button>
            </form>
        </div>
    </script>

    <script id="status_comment" type="handlebars-template">
        <span>{{ body }}</span>
    </script>

    <div id="feed">
        <h1>Feed</h1>
        <form class="basic" id="status_form" method="POST" action="" autocomplete="off">
            <textarea id="status" name="status">Ask something crazy!</textarea>
            <ul id="chosen_groups">
                <li>
                    <input id="choose_group_input" type="text" name="group"/>
                </li>
            </ul>
            <ul id="available_groups">
            </ul>
            <button class="dark" id="status_submit">submit</button>
        </form>
        <div id="statuses">
            % for status in statuses:
                <div class="status" id="status_${status.id}">
                    <div class="author">
                        <a href="/profile/${status.author.username}">${status.author.username}</a>
                    </div>
                    <span>${status.body}</span>
                    <ul class="actions">
                        <li>
                            <a class="add_comment">add comment</a>
                        </li>
                    </ul>
                    <div class="status_comments">
                        % for comment in status.comments:
                            <div class="status_comment" id="status_comment_${status.id}_${comment.id}">
                                <%
                                    last_rev = len(comment.history) - 1
                                %>
                                <span>${comment.history[last_rev].body}</span>
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