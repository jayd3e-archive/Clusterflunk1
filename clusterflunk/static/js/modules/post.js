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

    Post.Views.PostView = Backbone.View.extend({

        el: $("#post_view"),
        post_tree_view: undefined, // The list of top tier comments

        initialize: function() {
            post_comments = this.$el.children(".post_comment_tree");
            this.post_comment_tree = new Comment.Views.PostCommentsView({el: post_comments});
        },

        prompt: function(event) {
            return false;
        },

        persist: function() {
            return false;
        },

        add_comment: function(post_comment) {
            this.post_comment_tree(post_comment);
        }

    });

})(clusterflunk.module("post"));