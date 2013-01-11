// Models
window.Meal = Backbone.Model.extend();

window.MealCollection = Backbone.Collection.extend({
    model:Meal,
    url:"/api/meals/"
});


// Views
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


// Router
var AppRouter = Backbone.Router.extend({

    routes:{
        "":"list",
        "meals/:id":"mealDetails"
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
    }
});

var app = new AppRouter();
Backbone.history.start();