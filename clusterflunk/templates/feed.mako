<%inherit file="layouts/base.mako"/>
<%namespace name="status" file="statuses/status.mako"/>
<%namespace name="watchlist" file="aside/watchlist.mako"/>

<%def name="page()">
    <div class="feed">
        <h1>Feed</h1>
        <form class="basic status_form" method="POST" action="">
            <div class="error"></div>
            <textarea class="status" name="status">Ask something crazy!</textarea>
            <ul class="chosens">
                <li class="chosen">
                    Group Name
                </li>
                <li>
                    <input class="choose_input" type="text" name="group" autocomplete="off"/>
                </li>
            </ul>
            <ul class="availables">
                <li class="available">
                    Group Name
                </li>
            </ul>
            <button class="dark status_submit">submit</button>
        </form>
        <div class="statuses">
            ${ status.status() }
        </div>
    </div>
</%def>

<%def name="aside()">
    ${ watchlist.watchlist() }
</%def>