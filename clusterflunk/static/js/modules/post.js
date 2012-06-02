(function(Post) {

    /*
    *
    * Utilities
    *
    */

    Post.Parsers.Post = function (post) {
        var id = $(post).attr("id");
        id = id.split("_");
        post_id = id[1];

        return {id: post_id};
    };

    /*
    *
    * Models
    *
    */

    Post.Model = Backbone.Model.extend({

    });

    /*
    *
    * Dependencies
    *
    */

    Comment = clusterflunk.module("comment");

    /*
    *
    * Templates
    *
    */

    var post_comment_form_source = $("#post_comment_form").html();
    var post_comment_form_template = Handlebars.compile(post_comment_form_source);

    /*
    *
    * Views
    *
    */

    Post.Views.Post = Backbone.View.extend({

        el: $("#post_view"),
        post_tree_view: undefined, // The list of top tier comments
        events: {
            "click .post .add_comment": "prompt",
            "click .post button[name|='submit']": "persist"
        },

        initialize: function() {
            // Generate model
            post = this.$el.children(".post");
            attrs = Post.Parsers.Post(post);
            this.model = new Post.Model(attrs);

            post_comments = this.$el.children(".post_comment_tree");
            this.post_comment_tree = new Comment.Views.PostComments({el: post_comments});
        },

        prompt: function(event) {
            if (!this.$(".post .post_comment_form").length) {
                actions = this.$(".post .actions");
                context =  {post_id: this.model.get("id"),
                            parent_id: ""};
                $(post_comment_form_template(context)).insertAfter(actions);
            }
            return false;
        },

        persist: function() {
            var comment_form = this.$(".post .post_comment_form");

            var post_id = comment_form.find("input[name|='post_id']").val();
            var body = comment_form.find("textarea[name|='body']").val();

            var model = new Comment.Models.PostComment({post_id: post_id,
                                                      parent_id: "",
                                                      body: body});

            var that = this;
            model.save({}, {success: function(model, response) {
                that.$(".post .post_comment_form").remove();
                var post_comment = new Comment.Views.PostComment({model: model});
                that.add_comment(post_comment);
            }});

            return false;
        },

        add_comment: function(post_comment) {
            post_comment = post_comment.render();
            this.post_comment_tree.$el.append(post_comment.el);
        }

    });

})(clusterflunk.module("post"));