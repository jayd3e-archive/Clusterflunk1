<%namespace name="header_utils" file="../utilities/header.mako"/>

<%def name="header(here)">
    <a href="/">
        <div class="logo"></div>
    </a>
    <ul class="main_nav">
        <li>
            <button class="iconic chat_alt_fill"></button>
        </li>
    </ul>
    <div class="search">
        <input type="text" name="search"/>
        <button class="iconic magnifying_glass"></button>
    </div>
    <ul class="account">
        <li class="profile">
            <img class="avatar" src="/static/img/avatar.png" />
            <a href="/profile">jayd3e</a>
        </li>
        <li class="groups_list_button">
            groups
        </li>
        <li>
            <button class="post">post</button>
        </li>
    </ul>
    <div class="clear"></div>
    <ul class="group_list">
        <li>
            group 1
        </li>
        <li>
            group 2
        </li>
        <li>
            group 3
        </li>
    </ul>
</%def>
