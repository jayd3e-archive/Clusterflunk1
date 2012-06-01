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

    var post_comment_form_source = $("#post_comment_form").html();
    var post_comment_form_template = Handlebars.compile(post_comment_form_source);
    var post_comment_source = $("#post_comment").html();
    var post_comment_template = Handlebars.compile(post_comment_source);

    /*
    *
    * Models
    *
    */

    Comment.PostCommentModel = Backbone.Model.extend({
        url: "/comments/post"
    });

    Comment.StatusCommentModel = Backbone.Model.extend({
        url: "/comments/status"
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
        post_comments: undefined, // The PostComments contained in this PostComment

        initialize: function() {
            /*
            * Hack to get around the fact that jQuery.delegate() doesn't
            * accept the ("parent > child") selector
            * The equivalent of
            * event = {
            *      "click > .actions .add_reply": "prompt"
            * }
            */

            method = _.bind(this.prompt, this);
            this.$el.children(".actions").delegate('.add_comment', 'click', method);

            post_comments = this.$el.children(".post_comments");
            this.post_comments = new Comment.Views.PostCommentsView({el: post_comments});
        },

        render: function() {
            context = { id: this.model.get('id'),
                        post_id: this.model.get('post_id'),
                        parent_id: this.model.get('parent_id'),
                        body: this.model.get('body') };
            content = post_comment_template(context);
            this.$el.html(content);
            return this;
        },

        prompt: function(event) {
            if (!this.$(".post_comment_form").length) {
                actions = this.$el.children(".actions");
                context =  {post_id: this.model.get("post_id"),
                            parent_id: this.model.get("parent_id")};
                var post_comment_form = $(post_comment_form_template(context)).insertAfter(actions);

                // Same hack as above
                method = _.bind(this.persist, this);
                post_comment_form.delegate('.submit:button', 'click', method);
            }
            return false;
        },

        persist: function(event) {
            var comment_form = this.$el.children(".post_comment_form");

            var post_id = comment_form.find("input[name|='post_id']").val();
            var parent_id = comment_form.find("input[name|='parent_id']").val();
            var body = comment_form.find("textarea[name|='body']").val();

            var model = new Comment.PostCommentModel({post_id: post_id,
                                                      parent_id: parent_id,
                                                      body: body});

            var that = this;
            model.save({}, {success: function(model, response) {
                that.$el.children(".post_comment_form").remove();
                var post_comment = new Comment.Views.PostCommentView({model: model});
                that.post_comments.add_comment(post_comment);
            }});

            return false;
        }

    });

    Comment.Views.PostCommentsView = Backbone.View.extend({

        tagName: "div",
        className: "post_comments",

        initialize: function() {
            var post_comments = this.$el.children(".post_comment");
            $.each(post_comments, function(index, post_comment) {
                var attrs = Comment.Parsers.PostComment(post_comment);
                var model = new Comment.PostCommentModel(attrs);
                new Comment.Views.PostCommentView({el: post_comment, model: model});
            });
        },

        add_comment: function(post_comment) {
            post_comment = post_comment.render();
            this.$el.append(post_comment.el);
        }

    });

})(clusterflunk.module("comment"));