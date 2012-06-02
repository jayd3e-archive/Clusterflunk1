(function(Status) {
    /*
    *
    * Utilities
    *
    */

    Status.Parsers.Status = function(status) {
        var id = $(status).attr("id");
        id = id.split("_");
        status_id = id[1];

        return {id: status_id};
    };

    /*
    *
    * Templates
    *
    */

    var status_comment_form_source = $("#status_comment_form").html();
    var status_comment_form_template = Handlebars.compile(status_comment_form_source);

    /*
    *
    * Models
    *
    */

    Status.Model = Backbone.Model.extend({

        urlRoot: "statuses"

    });

    /*
    *
    * Views
    *
    */

    Status.Views.Statuses = Backbone.View.extend({
        el: $("#statuses"),

        initialize: function() {
            statuses = this.$el.children(".status");
            $.each(statuses, function(index, status) {
                attrs = Status.Parsers.Status(status);
                model = new Status.Model(attrs);
                new Status.Views.Status({el: status, model: model});
            });
        }
    });

    Status.Views.Status = Backbone.View.extend({
        className: "status",
        events: {
            "click .add_comment": "prompt"
        },

        initialize: function() {
            status_comments = this.$el.children(".status_comments");
            this.status_comments = new Status.Views.StatusComments({el: status_comments});
        },

        prompt: function() {
            if (!this.$("> .status_comment_form").length) {
                actions = this.$el.children(".actions");
                context =  {status_id: this.model.get("id")};
                $(status_comment_form_template(context)).insertAfter(actions);
            }
            return false;
        }
    });

    Status.Views.StatusComments = Backbone.View.extend({
        className: "status_comments",

        initialize: function() {
            status_comments = this.$el.children(".status_comment");
            $.each(status_comments, function(index, status_comment) {
                attrs = Comment.Parsers.StatusComment(status_comment);
                model = Comment.StatusCommentModel(attrs);
                new StatusComment({el: status_comment, model: model});
            });
        }
    });

    Status.Views.StatusComment = Backbone.View.extend({
        className: "status_comment"
    });

})(clusterflunk.module("status"));