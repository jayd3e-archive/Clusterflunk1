<%namespace name="header_utils" file="../utilities/header.mako"/>

<%def name="header(here)">
    <div class="logo"></div>
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
        <li>
            <a href="#">jayd3e</a>
        </li>
        <li>
            <div class="avatar"></div>
        </li>
        <li class="groups">
            Groups
            <ul class="group_list">
                <li>
                    Group 1
                </li>
                <li>
                    Group 2
                </li>
                <li>
                    Group 3
                </li>
            </ul>
        </li>
        <li>
            <button class="add">add</button>
        </li>
    </ul>
</%def>
