$(function() {
    var width = 242;

    $('.posts').masonry({
        itemSelector : '.post',
        columnWidth : width
    });

    $(window).resize(function() {
        var columns = Math.floor( $(window).width() / width );
        var actual_width = columns * width;
        if ($(".header").width() != actual_width) {
            $(".header").width(actual_width);
        }
        if ($(".posts").width() != actual_width) {
            $(".posts").width(actual_width);
        }
    });
});