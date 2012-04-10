<%inherit file="layouts/base.mako"/>
<%namespace name="util_side" file="utilities/side.mako"/>

<%def name="body()">
    <script id="status" type="handlebars-template">
        <div class="status">
            <div class="author">
                <a class="blue" href="/profile/{{username}}">
                    {{username}}
                </a>
            </div>
            {{body}}
        </div>
    </script>
    
    <div class="body_main centered">
        <h1>Feed</h1>
        <div class="status">
            <form id="status_form" method="POST" action="">
                <textarea id="status" name="status">Ask something crazy!</textarea>
                <input class="status_submit" id="submit" name="submit" type="submit"/>
            </form>
        </div>
        <div class="statuses">
            % for status in statuses:
                <div class="status">
                    <div class="author">
                        <a class="blue" href="/profile/${status.author.username}">
                            ${status.author.username}
                        </a>
                    </div>
                    ${status.body}
                </div>
            % endfor
        </div>
    </div>
</%def>

<%def name="side()">
    ${util_side.due()}
</%def>