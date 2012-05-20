<%inherit file="../layouts/landing.mako"/>
<%namespace name="util_error" file="../utilities/error.mako"/>

<%def name="page()">
    <div class="body_main centered">
        <form method="POST" action="">
            <div class="login">
                <h1 class="dark">Login</h1>
                ${ login_form.username(class_="login_text") }
                ${ util_error.error(login_form, 'username') }
                ${ login_form.password(class_="login_text") }
                ${ util_error.error(login_form, 'password') }
                <input class="submit" type="submit" name="submit" value="Login"/>
            </div>
        </form>
    </div>
</%def>