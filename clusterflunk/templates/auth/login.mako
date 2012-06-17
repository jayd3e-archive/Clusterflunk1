<%inherit file="../layouts/auth.mako"/>

<%def name="page()">
    <h1>Login</h1>
    <form class="basic" method="POST" action="">
        <label for="username">Username</label>
        <input name="username" type="text" />

        <label for="password">Password</label>
        <input name="password" type="password" />

        <input class="light" type="submit" name="submit" value="Login"/>
    </form>
</%def>