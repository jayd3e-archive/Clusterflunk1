(function(Comment) {

    /*
    *
    * Utilities
    *
    */

    Comment.Parsers.PostComment = function (comment) {
        var id = $(comment).attr("id");
        id = id.split("_");
        var post_id = id[2];
        var parent_id = id[3];

        return {post_id: post_id, parent_id: parent_id};
    };

    /*
    *
    * Templates
    *
    */

    var reply_source = $("#reply").html();
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

    Comment.Views.PostCommentView = Backbone.View.extend({

        tagName: "div",
        className: "post_comment",

        initialize: function() {
            // Hack to get around the fact that jQuery.delegate() doesn't
            // accept the ("parent > child") selector
            method = _.bind(this.prompt, this);
            this.$el.children(".actions").delegate('.add_reply', 'click', method);

            children = this.$el.children(".post_children").children(".post_child");
            $.each(children, function(index, child) {
                var attrs = Comment.Parsers.PostComment(child);
                var model = new Comment.PostCommentModel(attrs);
                new Comment.Views.PostChildView({el: child, model: model});
            });
        },

        prompt: function(event) {
            actions = this.$el.children(".actions");
            context =  {post_id: this.model.get("post_id"),
                        parent_id: this.model.get("parent_id")};
            var reply = $(reply_template(context)).insertAfter(actions);

            // Same hack here as above
            method = _.bind(this.persist, this);
            reply.delegate('.submit:button', 'click', method);
            return false;
        },

        persist: function() {
            return false;
        },

        remove_prompt: function() {

        }

    });

    Comment.Views.PostChildView = Comment.Views.PostCommentView.extend({

        className: "post_child",

    });

})(clusterflunk.module("comment"));