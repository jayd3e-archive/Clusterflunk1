<%inherit file="../layouts/auth.mako"/>

<%def name="page()">
    <h1>Register</h1>
    <form class="basic" method="POST" action="">
        <label for="username">Username</label>
        <input name="username" type="text" />

        <label for="password">Password</label>
        <input name="password" type="password" />

        <label for="repeat">Repeat</label>
        <input name="repeat" type="password" />

        <input class="light" type="submit" name="submit" value="Register"/>
    </form>
</%def>