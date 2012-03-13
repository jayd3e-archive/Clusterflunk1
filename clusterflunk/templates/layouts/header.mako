<%def name="header(here)">
    <div class="header_main centered">
        <div class="logo_container">
            <h1 class="light">
                <a class="logo" href="/">Clusterflunk</a>
            </h1>
        </div>
        <div class="main_nav">
            <ul>
                <li>
                    <a href="/groups">
                        <div id="groups"></div>
                    </a>
                </li>
                <li>
                    <a href="/articles">
                        <div id="articles"></div>
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
                    <a class="light" href="#">${user.username}</a>
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
