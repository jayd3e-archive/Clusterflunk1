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

/*
*
* Called at run-time
*
*/
jQuery(function($) {
    // Imports
    var app = clusterflunk.app;

    /*
    *
    * Utilities
    *
    */

    /*
    *
    * Main Router
    *
    */

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
            * Submit a reply
            *
            */

            submit_reply = function(event) {
                button = $(event.target);
                button.disabled = true;
                form = button.parent();

                post_id = form.children("input#post_id").val();
                parent_id = form.children("input#parent_id").val();
                reply = form.children("textarea#reply").val();

                data = {post_id : post_id,
                        parent_id : parent_id,
                        reply : reply}

                $.ajax({
                    type: "POST",
                    data: data,
                    url: "/posts/" + post_id,
                    success: function() {
                        $(".reply").remove(); // Remove all other replies
                    }
                });

                return false;
            }

            /*
            *
            * Add a reply input box under the comment
            *
            */

            add_reply = function(event) {
                $(".reply").remove(); // Remove all other replies
                link = $(event.target);
                post_actions = link.closest("div.post_actions");
                comment = link.closest("div.comment");
                id = comment.attr("id");
                id = id.split("_")
                post_id = id[1];
                parent_id = id[2];

                source   = $("#reply").html();
                template = Handlebars.compile(source);
                $(template({post_id:post_id, parent_id:parent_id})).insertAfter(post_actions);

                // Add the event to submit the reply
                $('input#submit').click(submit_reply);

                return false;
            }

            $('.add_reply').click(add_reply);

        }
    });

    app.router = new Router();
    Backbone.history.start({pushState: true});
});