(function(Status) {
    /*
    *
    * Dependencies
    *
    */

    Comment = clusterflunk.module("comment");

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
    var status_source = $("#status_template").html();
    var status_template = Handlebars.compile(status_source);

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
            "click .add_comment": "prompt",
            "click button[name|='submit']": "persist"
        },

        initialize: function() {
            status_comments = this.$el.children(".status_comments");
            this.status_comments = new Comment.Views.StatusComments({el: status_comments});
        },

        render: function() {
            context = {username: this.model.get("username"),
                       body: this.model.get("body")};
            this.$el.html(status_template(context));
            return this;
        },

        prompt: function() {
            if (!this.$("> .status_comment_form").length) {
                actions = this.$el.children(".actions");
                context =  {status_id: this.model.get("id")};
                $(status_comment_form_template(context)).insertAfter(actions);
            }
            return false;
        },

        persist: function() {
            var comment_form = this.$(".status_comment_form");

            var status_id = comment_form.find("input[name|='status_id']").val();
            var body = comment_form.find("textarea[name|='body']").val();

            var model = new Comment.Models.StatusComment({status_id: status_id,
                                                        body: body});

            var that = this;
            model.save({}, {success: function(model, response) {
                that.$(".status_comment_form").remove();
                var status_comment = new Comment.Views.StatusComment({model: model});
                that.add_comment(status_comment);
            }});

            return false;
        },

        add_comment: function(status_comment) {
            this.status_comments.add_comment(status_comment);
        }
    });

})(clusterflunk.module("status"));