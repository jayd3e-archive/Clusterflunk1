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
    var status_source = $("#status_template").html();
    var status_template = Handlebars.compile(status_source);

    /*
    *
    * Collections
    *
    */

    var AvailableGroups = Backbone.Collection.extend({
        model: Group.Model,
        url: function () {
            return "/groups?s=" + $("#choose_group_input").val();
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
        className: "chosen_group",

        render: function() {
            context = { name: this.model.get('name') };
            content = chosen_group_template(context);
            this.$el.html(content);
            return this;
        }

    });

    Feed.Views.AvailableGroup = Backbone.View.extend({
        tagName: "li",
        className: "available_group",

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
            "click #chosen_groups": "focus_chosen_groups_input",
            "keyup #choose_group_input": "get_available_groups",
            "click #status_submit": "submit"
        },

        initialize: function () {
            available_groups.bind("reset", this.render_all_available_groups, this);
            chosen_groups.bind("add", this.append_chosen_group, this);
        },

        focus_chosen_groups_input: function() {
            $("#choose_group_input").focus();
        },

        get_available_groups: function() {
            available_groups.fetch();
        },

        submit: function() {
            status_val = $("#status").val();
            chosen_group_ids = chosen_groups.pluck("id");
            status_model = new Status.Model({body: status_val, chosen_groups: chosen_group_ids});
            status_model.save({}, {success: function(model, response) {
                context = {username: model.get('username'),
                           body: model.get('body')};
                $("#statuses").prepend(status_template(context));
            }});

            // So the form doesn't get submited
            return false;
        },

        append_available_group: function(group) {
            available_group = new Feed.Views.AvailableGroup({model: group});
            this.$("#available_groups").append(available_group.render().el);
        },

        append_chosen_group: function(group) {
            chosen_group = new Feed.Views.ChosenGroup({model: group});
            this.$("#chosen_groups").prepend(chosen_group.render().el);
        },

        render_all_available_groups: function() {
            this.$("#available_groups").empty();
            available_groups.each(this.append_available_group);
            this.$("#available_groups").show();
        }

    });

    Feed.Views.FeedView = Backbone.View.extend({

        el: $("#feed"),

        initialize: function (options) {
            this.status_writer = new Feed.Views.StatusWriter();
        }

    });

})(clusterflunk.module("feed"));