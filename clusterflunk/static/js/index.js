/*
*
* Clusterflunk(frontend)
* Module system was inspired by a method described on http://weblog.bocoup.com
*
*/

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

Backbone.LayoutManager.configure({
   render:  function(template, context) {
       return Handlebars.compile(template)(context);
   }
});

jQuery(function($) {
    // Imports
    Auth = clusterflunk.module("auth")

    var app = clusterflunk.app;

    var Router = Backbone.Router.extend({
        routes: {
            "": "index"
        },

        index: function() {
            var landing = new Backbone.LayoutManager({
               name: "landing",
               template: "#landing",
               views: {
                   "#login": new Auth.Views.LoginView()
               }
            });

            landing.render(function(contents){
               $("#landing").html(contents); 
            });
        }
    });

    app.router = new Router();
    Backbone.history.start();

});