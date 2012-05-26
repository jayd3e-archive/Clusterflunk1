<%inherit file="../layouts/auth.mako"/>
<%namespace name="util_error" file="../utilities/error.mako"/>

<%def name="page()">
    <h1>Register</h1>
    <form method="POST" action="">
        ${ register_form.username() }
        ${ util_error.error(register_form, 'username') }

        ${ register_form.email() }
        ${ util_error.error(register_form, 'email') }

        ${ register_form.password() }
        ${ util_error.error(register_form, 'password') }
        
        ${ register_form.repeat_password() }
        ${ util_error.error(register_form, 'repeat_password') }
        <input type="submit" name="submit" value="Register"/>
    </form>
</%def>