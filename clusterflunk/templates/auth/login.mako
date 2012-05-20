<%inherit file="../layouts/landing.mako"/>
<%namespace name="util_error" file="../utilities/error.mako"/>

<%def name="page()">
    <h1>Login</h1>
    <form class="login" method="POST" action="">
        ${ login_form.username(class_="login_text") }
        ${ util_error.error(login_form, 'username') }
        
        ${ login_form.password(class_="login_text") }
        ${ util_error.error(login_form, 'password') }
        <input class="submit" type="submit" name="submit" value="Login"/>
    </form>
</%def>