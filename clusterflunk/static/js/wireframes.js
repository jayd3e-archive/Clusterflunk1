$(function() {
    $(".notifications_button").click(function(e) {
        $(".notifications").toggle();
    });

    $(".main_nav li > a").tipsy({
        opacity: 0.8
    });
});