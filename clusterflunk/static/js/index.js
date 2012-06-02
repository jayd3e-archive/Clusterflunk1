var clusterflunk = {
    module: function() {
        var modules = {};

        return function(name) {
            if (modules[name]) {
                return modules[name];
            }

            return modules[name] = { Views: {}, Parsers: {} };
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
    /* Changes the way arrays are serialized in jQuery.
       {foo: ["bar", "baz"]} will be serialized into "foo=bar&foo=baz" */
    traditional: true
});

/*
*
* Called at run-time
*
*/

$(function() {
    var app = clusterflunk.app;

    /*
    *
    * Main Router
    *
    */

    var Router = Backbone.Router.extend({

        routes: {
            "": "index",
            "groups": "groups",
            "groups?category=*category": "groups",
            "posts/:id": "posts"
        },

        initialize: function(options) {
            /*
            *
            * Global jQuery Behaviors
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
            };

            /*
            *
            * Global jQuery Events
            *
            */

            $("#notifications_button").click(notification_button);
        },

        index: function() {
            var Feed = clusterflunk.module("feed");
            var Status = clusterflunk.module("status");
            var feed = new Feed.Views.FeedView();
            var statuses = new Status.Views.Statuses();
        },

        groups: function() {
            var Group = clusterflunk.module("group");
            var group = new Group.Views.GroupListView();
        },

        posts: function(id) {
            var Post = clusterflunk.module("post");
            var post = new Post.Views.PostView();
        }

    });

    app.router = new Router();
    Backbone.history.start({pushState: true});
});
