<%inherit file="../layouts/small_base.mako"/>

<%def name="page()">
    <div class="networks">
        <div class="large_logo"></div>
        <form method="POST" action="">
            <input type="text" value="Networks" />
            <input class="primary" type="submit" value="Submit" />
        </form>
    </div>
</%def>