<%inherit file="../layouts/index_base.mako"/>
<%namespace name="util_error" file="../utilities/error.mako"/>

<%def name="page()">
    <div class="body_main centered">
        <form method="POST" action="">
            <div class="register">
                <h1>Register</h1>
                ${ register_form.username(class_="login_text") }
                ${ util_error.error(register_form, 'username') }
                ${ register_form.email(class_="login_text") }
                ${ util_error.error(register_form, 'email') }
                ${ util_register_form.password(class_="login_text") }
                ${ util_error.error(register_form, 'password') }
                ${ register_form.repeat_password(class_="login_text") }
                ${ util_error.error(register_form, 'repeat_password') }
                <input class="submit" type="submit" name="submit" value="Register"/>
            </div>
        </form>
    </div>
</%def>