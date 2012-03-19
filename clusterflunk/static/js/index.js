var clusterflunk = {
    module: function() {
        var modules = {};

        return function(name) {
            if (modules[name]) {
                return modules[name];
            }

            return modules[name] = { Views: {} };
        };
    }(),

    app: _.extend({}, Backbone.Events)
};

jQuery(function($) {
    // Imports
    var app = clusterflunk.app;

    var Router = Backbone.Router.extend({
        routes: {
            "groups?category=*category": "groups_category",
            "groups": "groups",
            "posts/:post_id": "posts_view"
        },

        groups: function() {
            /*
            *
            * Subscribed/Unsubscribe Buttons
            *
            */
            function toggle_subscription(event) {
                function toggle_button_class(data) {
                    if (data['status'] == 'unsubscribed') {
                        $(event.target).removeClass("button-small-negative");
                        $(event.target).addClass("button-small-positive");
                        $(event.target).text("subscribe");
                    }
                    else if (data['status'] == 'subscribed') {
                        $(event.target).removeClass("button-small-positive");
                        $(event.target).addClass("button-small-negative");
                        $(event.target).text("unsubscribe");
                    }
                }

                group_id = parseInt(event.target.id);
                if (group_id != undefined) {

                    if ($(event.target).hasClass("button-small-positive")) {
                        cmd = "subscribe";
                    }
                    else if ($(event.target).hasClass("button-small-negative")) {
                        cmd = "unsubscribe";
                    }

                    $.ajax({
                        type: "GET",
                        url: "/groups/" + group_id + "/" + cmd,
                        success: toggle_button_class
                    });
                }
            }

            $('.group button').click(toggle_subscription);
        },

        groups_category: function(category) {
            this.groups();
            
            /*
            *
            * Remove button when clicked on the 'mine' page.
            *
            */
            function remove_button(event) {
                group = $(event.target.parentNode);
                group.remove();
            }

            if (category == "mine") {
                $('.group button').click(remove_button);
            }

        },

        posts_view: function(post_id) {
            /*
            *
            * Add a reply input box under the comment
            *
            */

            add_reply = function(event) {
                $(".reply").remove(); // Remove all other replies
                link = $(event.target);
                comment = link.closest("div.post_actions");
                source   = $("#reply").html();
                template = Handlebars.compile(source);
                $(template()).insertAfter(comment);
            }

            $('.add_reply').click(add_reply);
        }
    });

    app.router = new Router();
    Backbone.history.start({pushState: true});
});