<%namespace name="header_utils" file="../utilities/header.mako"/>

<%def name="header(here)">
    <div id="logo"></div>
    <ul id="main_nav" class="horiz-nav">
        <li>
            <a id="notifications_button" href="#">&#xe007;</a>
            <div id="notifications">
                <div class="up_arrow"></div>
                <ul>
                    % for notification in notifications:
                        <li>
                            ${header_utils.print_notification(notification)}
                        </li>
                    % endfor
                </ul>
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
    <div id="search">
        <input type="text" name="search"/><button>&#xe074;</button>
    </div>
    <ul id="account">
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
