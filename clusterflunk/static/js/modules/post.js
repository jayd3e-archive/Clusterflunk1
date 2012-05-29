(function(Post) {

    /*
    *
    * Dependencies
    *
    */

    Comment = clusterflunk.module("comment");

    /*
    *
    * Models
    *
    */

    /*
    *
    * Collections
    *
    */

    /*
    *
    * Views
    *
    */

    Post.Views.PostTreeView = Backbone.View.extend({

        el: $("#post_view"),

        initialize: function() {
            post_comments = this.$(".post_comment");
            $.each(post_comments, function(index, post_comment) {
                var attrs = Comment.Parsers.PostComment(post_comment);
                var model = new Comment.PostCommentModel(attrs);
                new Comment.Views.PostCommentView({el: post_comment, model: model});
            });
        }

    });

})(clusterflunk.module("post"));