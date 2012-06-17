<%inherit file="layouts/base.mako"/>
<%namespace name="util_side" file="utilities/side.mako"/>

<%def name="page()">
    <script id="status_template" type="handlebars-template">
        <img class="thumbnail" src="/static/img/thumbnail.png"/>
        <div class="content">
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
        </div>
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
        <span>{{ body }}</span> -
        <a href="/profile/{{ username }}">{{ username }}</a>
        <span class="metadata">{{ created_timedelta }}</span>
    </script>

    <div id="feed">
        <h1>Feed</h1>
        <form class="basic" id="status_form" method="POST" action="">
            <div class="error"></div>
            <textarea id="status" name="status">Ask something crazy!</textarea>
            <ul class="chosens">
                <li>
                    <input class="choose_input" type="text" name="group" autocomplete="off"/>
                </li>
            </ul>
            <ul class="availables">
            </ul>
            <button class="dark" id="status_submit">submit</button>
        </form>
        <div id="statuses">
            <div class="status" id="status_1">
                <img class="thumbnail" src="/static/img/thumbnail.png"/>
                <div class="content">
                    <div class="author">
                        <a href="/profile/jayd3e">jayd3e</a>
                        <span class="metadata">2 days</span>
                    </div>
                    <span>This is a question.</span>
                    <ul class="actions">
                        <li>
                            <a class="add_comment">add comment</a>
                        </li>
                    </ul>
                    <div class="status_comments">
                        <div class="status_comment" id="status_comment_1_1">
                            <span>This is a comment.</span> -
                            <a href="/profile/jayd3e">jayd3e</a>
                            <span class="metadata">2 days</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</%def>

<%def name="aside()">
    ${util_side.due()}
</%def>