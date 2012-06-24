$(function() {
    var width = 232;
    var gutterWidth = 10;

    var resize_it = function() {
        var columns = Math.floor( ($(window).width() + 10) / (width + gutterWidth) );
        var actual_width = (columns * (width + gutterWidth)) - gutterWidth;
        if ($(".header").width() != actual_width) {
            $(".header").width(actual_width);
        }
        if ($(".posts").width() != actual_width) {
            $(".posts").width(actual_width);
        }
    };

    resize_it();
    $('.posts').masonry({
        itemSelector : '.post',
        columnWidth : width,
        gutterWidth: gutterWidth
    });

    $(window).resize(resize_it);
});