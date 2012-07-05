<%inherit file="../layouts/small_base.mako"/>

<%def name="page()">
    <div class="login">
        <div class="large_logo"></div>
        <form method="POST" action="">
            <input type="text" value="Username" />
            <input type="password" value="password" />
            <input class="primary" type="submit" value="Submit" />
        </form>
    </div>
</%def>