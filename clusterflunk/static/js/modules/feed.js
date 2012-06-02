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

        reset: function() {
            // Reset collections
            available_groups.reset();
            chosen_groups.reset();

            // Clean everything up
            this.$("#status").val("Ask something crazy!");
            this.$("#choose_group_input").val("");
            this.$("#chosen_groups .chosen_group").remove();
            this.$("#available_groups").empty();
            this.$("#available_groups").hide();
        },

        focus_chosen_groups_input: function() {
            $("#choose_group_input").focus();
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
                attrs = {username: model.get('username'),
                         body: model.get('body')};

                model = new Status.Model(attrs);
                status_view = new Status.Views.Status({model: model});
                that.add_status(status_view);
            }});

            this.reset();
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
        },

        add_status: function(status_view) {
            $("#statuses").prepend(status_view.render().el);
        }

    });

    Feed.Views.Feed = Backbone.View.extend({

        el: $("#feed"),

        initialize: function (options) {
            this.status_writer = new Feed.Views.StatusWriter();
        }

    });

})(clusterflunk.module("feed"));