(function(Status) {

    /*
    *
    * Models
    *
    */

    Status.Model = Backbone.Model.extend({

        urlRoot: "statuses"

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

    Status.Views.Statuses = Backbone.View.extend({

    });

    Status.Views.Status = Backbone.View.extend({

    });

    Status.Views.StatusComments = Backbone.View.extend({

    });

    Status.Views.StatusComment = Backbone.View.extend({

    });

})(clusterflunk.module("status"));