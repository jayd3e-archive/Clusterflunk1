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
    * Templates
    *
    */

    reply_source = $("#reply").html();
    reply_template = Handlebars.compile(reply_source);

    comment_source = $("#comment").html();
    comment_template = Handlebars.compile(comment_source);

    status_source = $("#status").html();
    status_template = Handlebars.compile(status_source);

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
            "": "index",
            "groups?category=*category": "groups_category",
            "groups": "groups",
            "posts/:post_id": "posts_view"
        },

        index: function() {
            
            /*
            *
            * Submit a status
            *
            */

            submit_status = function(event) {
                button = $(event.target);
                form = button.parent();
                body_main = form.closest(".body_main");
                statuses = body_main.children(".statuses");

                status = form.children("textarea#status").val();

                data = {status : status}

                $.ajax({
                  type: "POST",
                    data: data,
                    url: "/statuses",
                    success: function(data) {
                        context = {username : data['username'], body : data['body']};
                        $(statuses).prepend(status_template(context));
                    }
                });

                return false;
            }

            /*
            *
            * Once the "chosen_groups_container" is blurred, re-add the click event
            *
            */

            blur_choose_group = function(event) {
                $('.chosen_groups_container').unbind('blur');
            }

            /*
            *
            * Once the "chosen_groups_container" is clicked, create an input box
            *
            */

            choose_group = function(event) {
                $('#choose_group').html('<input type="text" name="group"/>');
                $('.chosen_groups_container').unbind('click');
                $('.chosen_groups_container').blur(blur_choose_group);
                $("#choose_group input").focus();
            }

            /*
            *
            * Bind Events
            *
            */

            $('.status_submit').click(submit_status);
            $('.chosen_groups_container').click(choose_group);  
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
                post_actions = link.closest("div.post_actions");
                comment = post_actions.parent();

                id = comment.attr("id");
                id = id.split("_")
                post_id = id[1];
                parent_id = id[2];

                context = {post_id : post_id, parent_id : parent_id};
                $(reply_template(context)).insertAfter(post_actions);

                // Add the event to submit the reply
                $('input#submit').click(submit_reply);

                return false;
            }

            /*
            *
            * Submit a reply
            *
            */

            submit_reply = function(event) {
                button = $(event.target);
                button.disabled = true;
                form = button.parent();
                parent = form.closest(".child, .comment, .post");
                children = parent.children(".children, .comments")

                post_id = form.children("input#post_id").val();
                parent_id = form.children("input#parent_id").val();
                body = form.children("textarea#body").val();

                data = {post_id : post_id,
                        parent_id : parent_id,
                        body : body}

                $.ajax({
                  type: "POST",
                    data: data,
                    url: "/comments/" + post_id,
                    success: function(data) {
                        $(".reply").remove(); // Remove all other replies
                        
                        context = {id : data['id'], post_id : data['post_id'], body : data['body']};
                        $(children).append(comment_template(context));
                        $(children).find('.add_reply').click(add_reply);
                    }
                });

                return false;
            }

            /*
            *
            * Bind Events
            *
            */

            $('.add_reply').click(add_reply);
        }
    });

    app.router = new Router();
    Backbone.history.start({pushState: true});
});