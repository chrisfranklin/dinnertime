// Models
window.Meal = Backbone.Model.extend();
window.Invite = Backbone.Model.extend();
window.Guest = Backbone.Model.extend();
// window.Part = Backbone.Model.extend();

window.MealCollection = Backbone.Collection.extend({
    model:Meal,
    url:"/api/meals/"
});
window.InviteCollection = Backbone.Collection.extend({
    model:Invite,
    url:"/api/invites/"
});
window.GuestCollection = Backbone.Collection.extend({
    model:Guest,
    url:"/api/guests/"
});
// window.PartCollection = Backbone.Collection.extend({
//     model:Part,
//     url:"/api/parts/"
// });


// Views Meals
window.MealListView = Backbone.View.extend({

    tagName:'ul',

    initialize:function () {
        this.model.bind("reset", this.render, this);
    },

    render:function (eventName) {
        _.each(this.model.models, function (meal) {
            $(this.el).append(new MealListItemView({model:meal}).render().el);
        }, this);
        return this;
    }

});

window.MealListItemView = Backbone.View.extend({

    tagName:"li",

    template:_.template($('#tpl-meal-list-item').html()),

    render:function (eventName) {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }

});

window.MealView = Backbone.View.extend({

    template:_.template($('#tpl-meal-details').html()),

    render:function (eventName) {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }

});

// Views Invites

window.InviteListView = Backbone.View.extend({

    tagName:'ul',

    initialize:function () {
        this.model.bind("reset", this.render, this);
    },

    render:function (eventName) {
        _.each(this.model.models, function (invite) {
            $(this.el).append(new InviteListItemView({model:invite}).render().el);
        }, this);
        return this;
    }

});

window.InviteListItemView = Backbone.View.extend({

    tagName:"li",

    template:_.template($('#tpl-invite-list-item').html()),

    render:function (eventName) {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }

});

window.InviteView = Backbone.View.extend({

    template:_.template($('#tpl-invite-details').html()),

    render:function (eventName) {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }

});


// Router
var AppRouter = Backbone.Router.extend({

    routes:{
        "":"list",
        "meals/:id":"mealDetails",
        "invites/":"ist",
        "invites/:id":"inviteDetails"
    },

    list:function () {
        this.mealList = new MealCollection();
        this.mealListView = new MealListView({model:this.mealList});
        this.mealList.fetch();
        $('#sidebar').html(this.mealListView.render().el);
    },

    mealDetails:function (id) {
        this.meal = this.mealList.get(id);
        this.mealView = new MealView({model:this.meal});
        $('#content').html(this.mealView.render().el);
    },

    ist:function () {
        this.inviteList = new InviteCollection();
        this.inviteListView = new InviteListView({model:this.inviteList});
        this.inviteList.fetch();
        $('#sidebar').html(this.inviteListView.render().el);
    },

    inviteDetails:function (id) {
        this.invite = this.inviteList.get(id);
        this.inviteView = new InviteView({model:this.invite});
        $('#content').html(this.inviteView.render().el);
    }

});

var app = new AppRouter();
Backbone.history.start();