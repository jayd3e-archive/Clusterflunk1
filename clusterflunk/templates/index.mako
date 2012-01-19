<!doctype html>
<html>
    <head>
        <title>Funky</title>
    </head>
    <body>
        <form id="login">
            <input type="text" name="login"/>
            <input type="password" name="password"/>
            <input type="submit" id="loginbutton" value="Log In"/>
        </form>

        <script src="${ request.static_url('clusterflunk:static/js/jquery-1.7.1.min.js') }"></script>
        <script>
            $('#login').submit(function () {
                var elem = this;
                $.post("${ request.route_url('api.login')}", {
                    'login': $('input[name="login"]', elem).val(),
                    'password': $('input[name="password"]', elem).val()
                })
                .success(function (data) {
                    if (data['status'] == 'logged_in') {
                        alert('success: '+data['userid']);
                    } else {
                        alert('failure!');
                    }
                })
                .error(function () {
                    alert('some other failure!');
                });
                return false;
            });
        </script>
    </body>
</html>
