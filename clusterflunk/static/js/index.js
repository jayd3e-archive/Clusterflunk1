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
* jQuery Settings
*
*/
$.ajaxSetup({
  traditional: true
});

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
    * Global Behaviors
    *
    */
    notification_button = function() {
        $("#notifications").toggle();
        if ($("#notifications_button").hasClass("active")) {
            $("#notifications_button").removeClass("active");
        }
        else {
            $("#notifications_button").addClass("active");
        }
    }

    /*
    *
    * Global Events
    *
    */
    $("#notifications_button").click(notification_button);


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
            "groups/create": "groups_create",
            "posts/:post_id": "posts_view"
        },

        index: function() {

            /*
            *
            * Local Vars
            *
            */
            available_groups = []
            chosen_groups = []

            /*
            *
            * Local Functions
            *
            */

            add_group = function(group) {
                chosen_groups.push(group);
            }

            /*
            *
            * Templates
            *
            */

            status_source = $("#status_template").html();
            status_template = Handlebars.compile(status_source);

            chosen_group_source = $("#chosen_group_template").html();
            chosen_group_template = Handlebars.compile(chosen_group_source);

            reply_source = $("#reply").html();
            reply_template = Handlebars.compile(reply_source);

            status_comment_source = $("#status_comment").html();
            status_comment_template = Handlebars.compile(status_comment_source);
            
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

                status_value = form.children("textarea#status").val();

                chosen_group_ids = []
                $.each(chosen_groups, function(index, chosen_group) {
                    chosen_group_ids.push(chosen_group.id)
                });
                data = {status : status_value, chosen_groups : chosen_group_ids}

                $.ajax({
                    type: "POST",
                    data: data,
                    url: "/statuses",
                    success: function(data) {
                        context = {username : data['username'], body : data['body']};
                        $(statuses).prepend(status_template(context));
                    }
                });

                $('.chosen_group').remove();
                $("#status").val("Ask something crazy!");

                return false;
            }

            /*
            *
            * Once the "chosen_groups_container" is clicked, focus the input box
            *
            */

            choose_group = function(event) {
                $("#choose_group_input").focus();
            }

            /*
            *
            * Add a reply input box under the status
            *
            */

            add_reply = function(event) {
                $(".reply").remove(); // Remove all other replies
                link = $(event.target);
                status_actions = link.closest("div.status_actions");
                status_div = status_actions.parent();

                id = status_div.attr("id");
                id = id.split("_");
                status_id = id[1];

                context = {status_id : status_id};
                $(reply_template(context)).insertAfter(status_actions);

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
                parent = form.closest(".status");
                children = parent.find(".status_comments");

                status_id = form.children("input#status_id").val();
                body = form.children("textarea#body").val();

                data = {status_id : status_id,
                        body : body}

                $.ajax({
                  type: "POST",
                    data: data,
                    url: "/comments/status/" + status_id,
                    success: function(data) {
                        $(".reply").remove(); // Remove all other replies
                        
                        context = {id : data['id'], body : data['body']};
                        $(children).append(status_comment_template(context));
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

            $('.status_submit').click(submit_status);
            $('.chosen_groups_container').click(choose_group);
            $("#choose_group_input").autocomplete({
                source: function(request, response) {
                    $.ajax({
                        url: "/groups?s=" + request.term,
                        success: function(data) {
                            available_groups = [];
                            response($.map(data, function(group) {
                               
                               available_group = {
                                   id : group.id,
                                   name : group.name
                               };
                               available_groups.push(available_group);

                               return {
                                   label: group.name,
                                   value: group.name
                               }
                            }));
                        }
                    });
                },
                select: function(event, ui) {
                    item = {}
                    $.each(available_groups, function(index, group) {
                        if (group['name'] == ui.item['label']) {
                            item = group;
                            return;
                        }
                    });
                    group = {id : item['id'], name : item['name']};
                    add_group(group);

                    context = {label : ui.item['label']};
                    $("#chosen_groups_input").before(chosen_group_template(context));
                    $("#choose_group_input").val('');
                    $('#choose_group_input').focus();
                    return false;
                },
            });
            $('.add_reply').click(add_reply);
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
                        $(event.target).removeClass("default");
                        $(event.target).addClass("primary");
                        $(event.target).text("subscribe");
                    }
                    else if (data['status'] == 'subscribed') {
                        $(event.target).removeClass("primary");
                        $(event.target).addClass("default");
                        $(event.target).text("unsubscribe");
                    }
                }

                group_id = parseInt(event.target.id);
                if (group_id != undefined) {

                    if ($(event.target).hasClass("primary")) {
                        cmd = "subscribe";
                    }
                    else if ($(event.target).hasClass("default")) {
                        cmd = "unsubscribe";
                    }

                    $.ajax({
                        type: "GET",
                        url: "/groups/" + group_id + "/" + cmd,
                        success: toggle_button_class
                    });
                }
            }

            /*
            *
            * Link to the 'Create Group' page
            *
            */

            function group_link(event) {
                $("#create_group_form").submit();
            }

            /*
            *
            * Bind Events
            *
            */

            $('.group button').click(toggle_subscription);
            $('#create_group').click(group_link);
        },

        groups_create: function() {

            /*
            *
            * Local Vars
            *
            */
            available_users = []
            invites = []

            /*
            *
            * Templates
            *
            */

            invite_source = $("#invite_template").html();
            invite_template = Handlebars.compile(invite_source);

            /*
            *
            * Local Functions
            *
            */

            add_user = function(user) {
                invites.push(user);
            }

            /*
            *
            * Once the "invites_container" is clicked, focus the input box
            *
            */

            invites = function(event) {
                $("#invite_input").focus();
            }


            /*
            *
            * Bind Events
            *
            */

            $('.invites_container').click(invites);
            $("#invite_input").autocomplete({
                source: function(request, response) {
                    $.ajax({
                        url: "/users?s=" + request.term,
                        success: function(data) {
                            invites = [];
                            response($.map(data, function(user) {
                               
                               available_user = {
                                   id : user.id,
                                   username : user.username
                               };
                               available_users.push(available_user);

                               return {
                                   label: user.username,
                                   value: user.username
                               }
                            }));
                        }
                    });
                },
                select: function(event, ui) {
                    item = {}
                    $.each(available_users, function(index, user) {
                        if (user['username'] == ui.item['label']) {
                            item = user;
                            return;
                        }
                    });

                    user = {id : item['id'], name : item['username']};
                    add_user(user);

                    context = {label : item['username'], id : item['id']};
                    $("#invite_input").before(invite_template(context));
                    $("#invite_input").val('');
                    $('#invite_input').focus();
                    return false;
                },
            });
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
            * Templates
            *
            */

            reply_source = $("#reply").html();
            reply_template = Handlebars.compile(reply_source);

            comment_source = $("#comment").html();
            comment_template = Handlebars.compile(comment_source);

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
                    url: "/comments/post/" + post_id,
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