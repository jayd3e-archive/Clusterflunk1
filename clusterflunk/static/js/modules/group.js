(function(Group) {
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

})(clusterflunk.module("group"));