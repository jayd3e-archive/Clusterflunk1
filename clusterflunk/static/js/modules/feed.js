(function(Feed) {
    /*
    *
    * Dependencies
    *
    */

    var Group = clusterflunk.module("group");
    var Status = clusterflunk.module("status");

    /*
    *
    * Templates
    *
    */

    var available_group_source = $("#available_group_template").html();
    var available_group_template = Handlebars.compile(available_group_source);
    var chosen_group_source = $("#chosen_group_template").html();
    var chosen_group_template = Handlebars.compile(chosen_group_source);

    /*
    *
    * Collections
    *
    */

    var AvailableGroups = Backbone.Collection.extend({
        model: Group.Model,
        url: function () {
            return "/groups?s=" + $(".chosens .choose_input").val();
        }
    });

    var ChosenGroups = Backbone.Collection.extend({
        model: Group.Model
    });

    /*
    *
    * Module Vars
    *
    */

    var available_groups = new AvailableGroups();
    var chosen_groups = new ChosenGroups();

    /*
    *
    * Views
    *
    */

    Feed.Views.ChosenGroup = Backbone.View.extend({
        tagName: "li",
        className: "chosen",

        render: function() {
            context = { name: this.model.get('name') };
            content = chosen_group_template(context);
            this.$el.html(content);
            return this;
        }

    });

    Feed.Views.AvailableGroup = Backbone.View.extend({
        tagName: "li",
        className: "available",

        events: {
            "click": "pick"
        },

        render: function() {
            context = { name: this.model.get('name').substring(0, 15) };
            content = available_group_template(context);
            this.$el.html(content);
            return this;
        },

        pick: function() {
            chosen_groups.add(this.model);
        }

    });

    Feed.Views.StatusWriter = Backbone.View.extend({

        el: $("#status_form"),

        events: {
            "click .chosens": "focus_chosen_groups_input",
            "keyup .chosens .choose_input": "get_available_groups",
            "click #status_submit": "submit"
        },

        initialize: function () {
            available_groups.bind("reset", this.render_all_available_groups, this);
            chosen_groups.bind("add", this.append_chosen_group, this);
        },

        reset: function() {
            // Reset collections
            available_groups.reset();
            chosen_groups.reset();

            // Clean everything up
            this.$(".error").hide();
            this.$("#status").val("Ask something crazy!");
            this.$(".chosens .choose_input").val("");
            this.$(".chosens .chosen").remove();
            this.$(".availables").empty();
            this.$(".availables").hide();
        },

        focus_chosen_groups_input: function() {
            $(".chosens .choose_input").focus();
        },

        get_available_groups: function() {
            available_groups.fetch();
        },

        submit: function() {
            var status_val = $("#status").val();
            var chosen_group_ids = chosen_groups.pluck("id");
            var status_model = new Status.Model({body: status_val,
                                                 chosen_groups: chosen_group_ids});

            that = this;
            status_model.save({}, {success: function(model, response) {
                status_view = new Status.Views.Status({model: model});
                that.add_status(status_view);
                that.reset();
            },
            error: function(model, response) {
                that.error(response);
            }});

            // So the form doesn't get submited
            return false;
        },

        error: function(msg) {
            this.$(".error").show().html(msg);
        },

        append_available_group: function(group) {
            available_group = new Feed.Views.AvailableGroup({model: group});
            this.$(".availables").append(available_group.render().el);
        },

        append_chosen_group: function(group) {
            chosen_group = new Feed.Views.ChosenGroup({model: group});
            this.$(".chosens").prepend(chosen_group.render().el);
        },

        render_all_available_groups: function() {
            this.$(".availables").empty();
            available_groups.each(this.append_available_group);
            this.$(".availables").show();
        },

        add_status: function(status_view) {
            $("#statuses").prepend(status_view.render().el);
            MathJax.Hub.Queue(["Typeset", MathJax.Hub, status_view.el]);
        }

    });

    Feed.Views.Feed = Backbone.View.extend({

        el: $("#feed"),

        initialize: function (options) {
            this.status_writer = new Feed.Views.StatusWriter();
        }

    });

})(clusterflunk.module("feed"));