<%inherit file="../layouts/small_base.mako"/>

<%def name="page()">
    <div class="login">
        <div class="large_logo"></div>
        <div class="social_connects">
            <a class="facebook" href="#"></a>
            <a class="twitter" href="#"></a>
            <div class="clear"></div>
        </div>
        <form method="POST" action="">
            <input type="text" value="Username" />
            <input style="margin-bottom: 5px;" type="password" value="password" />
            <a style="display: block; margin-bottom: 7px; font-size: 15px;" href="/forgot">Feeling forgetful?</a>
            <input class="primary" type="submit" value="Submit" />
        </form>
    </div>
</%def>