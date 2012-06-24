<%namespace name="header_utils" file="../utilities/header.mako"/>

<%def name="header(here)">
    <a class="logo" href="/"></a>
    <ul class="main_nav">
        <li>
            <a class="notifications_button" href="#" original-title="notifications">&#xe007;</a>
            <ul class="notifications">
                <div class="up_arrow"></div>
                <li class="notification">
                    <a href="/profile/jayd3e">jayd3e</a>
                    invited you to
                    <a href="/groups/1">group</a>
                </li>
                <li class="notification">
                    <a href="/profile/jayd3e">jayd3e</a>
                    commented on a
                    <a href="/statuses/1">status</a>
                    you interacted with.
                </li>
            </ul>
        </li>
        <li>
            <a href="/posts" original-title="posts">&#xe005;</a>
        </li>
        <li>
            <a href="/groups" original-title="groups">&#xe062;</a>
        </li>
    </ul>
    <div class="search">
        <input type="text" name="search" autocomplete="off"/><button>&#xe074;</button>
    </div>
    <ul class="account">
        <li>
            <a href="/profile">jayd3e</a>
        </li>
        <li>
            <a class="avatar" href="/profile">
                <img src="/static/img/avatar.png"/>
            </a>
        </li>
        <li>
            <a class="add" href="/profile">add</a>
        </li>
    </ul>
</%def>
