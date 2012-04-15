<%def name="header(here)">
    <div class="header_main centered">
        <div class="logo_container">
            <a href="/">
                <div class="logo"></div>
            </a>
        </div>
        <div class="main_nav">
            <ul>
                <li>
                    <a class="light" href="/posts">
                        hw
                    </a>
                </li>
                <li>
                    <a class="light" href="/groups">
                        groups
                    </a>
                </li>
                <li>
                    <a class="light" href="/articles">
                        articles
                    </a>
                </li>
            </ul>
        </div>
        <div class="side_nav">
            <ul>
                <li>
                    <a class="light" href="/logout">logout</a>
                </li>
                <li>
                    <a class="light" href="#">network</a>
                </li>
                <li id="username">
                    <a class="light" href="/profile">${user.username}</a>
                </li>
                <li id="avatar">
                    <a href="">
                        <img src="/static/img/avatar.png" />
                    </a>
                </li>
            </ul>
        </div>
    </div>
</%def>
