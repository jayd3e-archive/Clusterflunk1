(function(Comment) {

    /*
    *
    * Utilities
    *
    */

    parse_comment = function (comment) {
        var id = comment.attr("id");
        id = id.split("_");
        var post_id = id[1];
        var parent_id = id[2];

        return {post_id: post_id, parent_id: parent_id};
    };

    /*
    *
    * Templates
    *
    */

    var reply_source = $("#reply_template").html();
    var reply_template = Handlebars.compile(reply_source);

    /*
    *
    * Models
    *
    */

    Comment.PostCommentModel = Backbone.Model.extend({
        urlRoot: "comments/post"
    });

    Comment.StatusCommentModel = Backbone.Model.extend({
        urlRoot: "comments/status"
    });

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

    Comment.Views.CommentView = Backbone.Model.extend({

        tagName: "div",
        className: "comment",

        events: {
            "click .add_reply": "prompt"
        },

        prompt: function(event) {
            post_actions = this.$el.children(".post_actions");
            $(reply_template()).insertAfter(post_actions);
            return false;
        }

    });

    Comment.Views.ChildView = Comment.Views.CommentView.extend({

        className: "child"

    });

})(clusterflunk.module("comment"));