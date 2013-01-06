'use strict';

var slApp = angular.module('slApp', ['ngResource', 'ui','ui.directives', 'ui.filters'], 
    function($routeProvider, $locationProvider) {
        $routeProvider
          .when('/', {
            templateUrl: 'static/templates/index.html',
            controller: HomeCtrl
          })
          .when('/category/:categorySlug', {
            templateUrl: 'static/templates/browse.html',
            controller: SystemListCtrl,
          })
          .when('/latest', {
            templateUrl: 'static/templates/browse.html',
            controller: LatestSystemListCtrl,
          })
          .when('/recent', {
            templateUrl: 'static/templates/browse.html',
            controller: UpdatedSystemListCtrl,
          })
          .when('/search', {
            templateUrl: 'static/templates/browse.html',
            controller: SystemSearchCtrl,
            reloadOnSearch:false,
          })
          .when('/system/:systemSlug', {
            templateUrl: 'static/templates/system-detail.html',
            controller: SystemDetailCtrl
          })
          .otherwise({
            redirectTo: '/'
          });
  });

slApp.run(function($rootScope, $http) {
});
angular.injector(['ng']).invoke(function($rootScope, $http) {
    $http.get('stack/api/v1/category/?format=json').success(function(result){
         $rootScope.categories = result;
    });
});
