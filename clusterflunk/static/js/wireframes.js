$(function() {
    var width = 232;
    var gutterWidth = 10;

    var resize_it = function() {
        var columns = Math.floor( ($(window).width() + 10) / (width + gutterWidth) );
        var actual_width = (columns * (width + gutterWidth)) - gutterWidth;
        if ($(".posts, .groups, .header, .group_view > .inner").width() != actual_width) {
            $(".posts, .groups, .header, .group_view > .inner").width(actual_width);
        }
    };

    resize_it();
    $('.posts, .groups').masonry({
        itemSelector : '.post, .group',
        columnWidth : width,
        gutterWidth: gutterWidth
    });

    $(window).resize(resize_it);
});