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
            post_comments = this.$el.children(".post_comment_tree");
            new Comment.Views.PostCommentsView({el: post_comments});
        }

    });

})(clusterflunk.module("post"));