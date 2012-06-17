<%namespace name="header_utils" file="../utilities/header.mako"/>

<%def name="header(here)">
    <a href="/" id="logo"></a>
    <ul id="main_nav">
        <li>
            <a id="notifications_button" href="#" original-title="notifications">&#xe007;</a>
            <div id="notifications">
                <div class="up_arrow"></div>
                <ul>
                    <li>
                        <div class="notification">
                            <div class="group_invite_notification">
                                <a href="/profile/jayd3e">
                                    jayd3e
                                </a>
                                invited you to
                                <a href="/groups/1">
                                    group
                                </a>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="notification">
                            <div class="status_comment_notification">
                                <a href="/profile/jayd3e">
                                    jayd3e
                                </a>
                                commented on a
                                <a href="/statuses/1">
                                    status
                                </a>
                                you interacted with.
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </li>
        <li>
            <a href="/posts" original-title="posts">&#xe005;</a>
        </li>
        <li>
            <a href="/groups" original-title="groups">&#xe062;</a>
        </li>
    </ul>
    <div id="search">
        <input type="text" name="search" autocomplete="off"/><button>&#xe074;</button>
    </div>
    <ul id="account">
        <li>
            <a href="/logout">sign out</a>
        </li>
        <li>
            <a href="/profile/jayd3e">jayd3e</a>
        </li>
        <li>
            <a class="avatar" href="/profile">
                <img src="/static/img/avatar.png"/>
            </a>
        </li>
    </ul>
</%def>
