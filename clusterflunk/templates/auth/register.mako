<%inherit file="../layouts/landing.mako"/>
<%namespace name="util_error" file="../utilities/error.mako"/>

<%def name="page()">
    <h1>Register</h1>
    <form  class="register" method="POST" action="">
        ${ register_form.username(class_="login_text") }
        ${ util_error.error(register_form, 'username') }

        ${ register_form.email(class_="login_text") }
        ${ util_error.error(register_form, 'email') }

        ${ register_form.password(class_="login_text") }
        ${ util_error.error(register_form, 'password') }
        
        ${ register_form.repeat_password(class_="login_text") }
        ${ util_error.error(register_form, 'repeat_password') }
        <input class="submit" type="submit" name="submit" value="Register"/>
    </form>
</%def>