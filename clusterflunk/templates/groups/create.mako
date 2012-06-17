<%inherit file="../layouts/base.mako"/>
<%namespace name="watchlist" file="../aside/watchlist.mako"/>

<%def name="page()">
    <div class="group_create">
        <form class="basic" action="" method="POST">
            <div class="error"></div>
            <input type="text" class="name" autocomplete="off" value="Group Name" />
            <ul class="page_actions">
                <li>
                    <a class="primary" href="/posts/create">Create Post</a>
                </li>
            </ul>
            <span class="metadata">
                created by
                <a href="/profile/jayd3e">jayd3e</a>
                right now
            </span>
            <textarea class="description" autocomplete="off">Description</textarea>
            <ul class="chosens">
                <li class="chosen">
                    Chosen Group
                </li>
                <li>
                    <input class="choose_input" type="text" name="user" autocomplete="off"/>
                </li>
            </ul>
            <ul class="availables">
                <li class="available">
                    Available Group
                </li>
            </ul>
            <button class="dark create_submit">submit</button>
        </form>
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>