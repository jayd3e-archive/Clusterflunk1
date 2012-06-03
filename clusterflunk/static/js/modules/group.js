(function(Group) {
    /*
    *
    * Dependencies
    *
    */

    User = clusterflunk.module('user');

    /*
    *
    * Utilities
    *
    */

    // Given a DOM object that represents a group, will parse out
    // all information from the DOM to create a Model.
    Group.Parsers.Group = function (group) {
        // id
        var parts = group.id.split("_");
        var group_id = parts[1];

        // name
        var group_name_link = $(group).children(".group_name").first();
        var name = group_name_link.html();

        return {id: group_id, name: name};
    };

    /*
    *
    * Templates
    *
    */

    var available_user_source = $("#available_user_template").html();
    var available_user_template = Handlebars.compile(available_user_source);
    var chosen_user_source = $("#chosen_user_template").html();
    var chosen_user_template = Handlebars.compile(chosen_user_source);

    /*
    *
    * Models
    *
    */

    Group.Model = Backbone.Model.extend({

        urlRoot: "groups"

    });

    /*
    *
    * Collections
    *
    */

    var AvailableUsers = Backbone.Collection.extend({
        model: Group.Model,
        url: function () {
            return "/users?s=" + $(".chosens .choose_input").val();
        }
    });

    var ChosenUsers = Backbone.Collection.extend({
        model: User.Model
    });

    /*
    *
    * Module Vars
    *
    */

    var available_users = new AvailableUsers();
    var chosen_users = new ChosenUsers();

    /*
    *
    * Views
    *
    */

    Group.Views.GroupCondensed = Backbone.View.extend({

        events: {
            "click .group button.primary": "subscribe",
            "click .group button.dark": "unsubscribe"
        },

        subscribe: function(event) {
            $.ajax({
                type: "GET",
                url: "/groups/" + this.model.id + "/subscribe",
                success: function() {
                    $(event.target).addClass("dark");
                    $(event.target).removeClass("primary");
                    $(event.target).text("unsubscribe");
                }
            });
        },

        unsubscribe: function(event) {
            $.ajax({
                type: "GET",
                url: "/groups/" + this.model.id + "/unsubscribe",
                success: function() {
                    $(event.target).addClass("primary");
                    $(event.target).removeClass("dark");
                    $(event.target).text("subscribe");
                }
            });
        }

    });

    Group.Views.GroupList = Backbone.View.extend({

        el: $("#groups"),

        initialize: function() {
            that = this;
            var groups = this.$(".group");
            $.each(groups, function(index, group) {
                attrs = Group.Parsers.Group(group);
                model = new Group.Model(attrs);
                var options = {el: group, model: model};
                new Group.Views.GroupCondensed(options);
            });
        }

    });

    Group.Views.ChosenUser = Backbone.View.extend({
        tagName: "li",
        className: "chosen",

        render: function() {
            context = {id: this.model.get("id "),
                       username: this.model.get('username')};
            content = chosen_user_template(context);
            this.$el.html(content);
            return this;
        }

    });

    Group.Views.AvailableUser = Backbone.View.extend({
        tagName: "li",
        className: "available",

        events: {
            "click": "pick"
        },

        render: function() {
            context = { username: this.model.get('username') };
            content = available_user_template(context);
            this.$el.html(content);
            return this;
        },

        pick: function() {
            chosen_users.add(this.model);
        }

    });

    Group.Views.GroupCreate = Backbone.View.extend({

        el: $("#group_create"),
        events: {
            "click .chosens": "focus_chosen_users_input",
            "keyup .chosens .choose_input": "get_available_users"
        },

        initialize: function () {
            available_users.bind("reset", this.render_all_available_users, this);
            chosen_users.bind("add", this.append_chosen_user, this);
        },

        focus_chosen_users_input: function() {
            $(".chosens .choose_input").focus();
        },

        get_available_users: function() {
            available_users.fetch();
        },

        append_available_user: function(user) {
            available_user = new Group.Views.AvailableUser({model: user});
            this.$(".availables").append(available_user.render().el);
        },

        append_chosen_user: function(user) {
            chosen_user = new Group.Views.ChosenUser({model: user});
            this.$(".chosens").prepend(chosen_user.render().el);
        },

        render_all_available_users: function() {
            this.$(".availables").empty();
            available_users.each(this.append_available_user);
            this.$(".availables").show();
        }

    });

})(clusterflunk.module("group"));