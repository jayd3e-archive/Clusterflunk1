<%inherit file="../layouts/small_base.mako"/>

<%def name="page()">
    <div class="register">
        <div class="large_logo"></div>
        <form method="POST" action="/networks">
            <input type="text" value="Username" />
            <input type="text" value="E-mail" />
            <input type="password" value="password" />
            <input class="primary" type="submit" value="Submit" />
        </form>
    </div>
</%def>