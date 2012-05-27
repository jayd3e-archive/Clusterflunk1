<%inherit file="layouts/base.mako"/>
<%namespace name="util_side" file="utilities/side.mako"/>

<%def name="page()">
    <script id="status_template" type="handlebars-template">
        <div class="status">
            <div class="author">
                <a href="/profile/{{username}}">
                    {{username}}
                </a>
            </div>
            {{body}}
        </div>
    </script>

    <script id="chosen_group_template" type="handlebars-template">
        <li class="chosen_group">{{label}}</li>
    </script>

    <script id="reply" type="handlebars-template">
        <div class="reply">
            <form class="basic" id="reply_form" method="POST" action="">
                <input id="status_id" name="parent_id" type="hidden" value="{{status_id}}"/>
                <textarea id="body" name="body"></textarea>
                <input id="submit" name="submit" type="submit"/>
            </form>
        </div>
    </script>

    <script id="status_comment" type="handlebars-template">
        <div class="status_comment">
            {{body}}
        </div>
    </script>
    
    <div class="body_main centered">
        <div class="main_heading">
            <h1>Feed</h1>
        </div>
        <div class="status">
            <form class="basic" id="status_form" method="POST" action="">
                <textarea id="status" name="status">Ask something crazy!</textarea>
                <div class="chosen_groups_container">
                    <ul class="chosen_groups">
                        <li class="chosen_groups_input" id="chosen_groups_input">
                            <input id="choose_group_input" type="text" name="group"/>
                        </li>
                    </ul>
                </div>
                <input class="status_submit" id="submit" name="submit" type="submit"/>
            </form>
        </div>
        <div class="statuses">
            % for status in statuses:
                <div id="status_${status.id}" class="status">
                    <div class="author">
                        <a href="/profile/${status.author.username}">
                            ${status.author.username}
                        </a>
                    </div>
                    ${status.body}
                    <div class="status_actions">
                        <ul>
                            <li>
                                <a class="add_reply">add comment</a>
                            </li>
                        </ul>
                    </div>
                    <div class="status_comments">
                        % for comment in status.comments:
                            <div class="status_comment">
                                <%
                                    last_rev = len(comment.history) - 1
                                %>
                                ${comment.history[last_rev].body}
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