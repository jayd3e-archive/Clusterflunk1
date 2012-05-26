<%namespace name="header_utils" file="../utilities/header.mako"/>

<%def name="header(here)">
    <div>
    </div>
    <ul>
        <li>
            <div id="notifications_button" class="notifications_button">
                <a href="#">&#xe007;</a>
            </div>
            <div id="notifications_list" class="notifications_list">
                <ul>
                    % for notification in notifications:
                        <li>
                            ${header_utils.print_notification(notification)}
                        </li>
                    % endfor
                </ul>
                <div class="up_arrow">
                </div>
            </div>
        </li>
        <li>
            <a href="/posts">&#xe005;</a>
        </li>
        <li>
            <a href="/groups">&#xe062;</a>
        </li>
        <li>
            <a href="/articles">&#xe000;</a>
        </li>
    </ul>
    <div class="search">
        <input type="text" name="search"/><button>&#xe074;</button>
    </div>
    <ul class="account">
        <li>
            <a href="/logout">sign out</a>
        </li>
        <li>
            <a href="/profile">${user.username}</a>
        </li>
        <li>
            <a class="avatar" href="/profile">
                <img src="/static/img/avatar.png"/>
            </a>
        </li>
    </ul>
</%def>
