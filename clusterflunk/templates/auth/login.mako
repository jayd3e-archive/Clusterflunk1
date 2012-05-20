<%inherit file="../layouts/auth.mako"/>
<%namespace name="util_error" file="../utilities/error.mako"/>

<%def name="page()">
    <h1>Login</h1>
    <form class="basic" method="POST" action="">
        ${ login_form.username.label }
        ${ login_form.username() }
        ${ util_error.error(login_form, 'username') }

        ${ login_form.password.label }
        ${ login_form.password() }
        ${ util_error.error(login_form, 'password') }
        
        <input class="primary" type="submit" name="submit" value="Login"/>
    </form>
</%def>