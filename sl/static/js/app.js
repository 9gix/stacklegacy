'use strict';

var slApp = angular.module('slApp', ['ngResource', 'ui','ui.directives', 'ui.filters'], 
    function($routeProvider, $locationProvider) {
        $routeProvider
          .when('/', {
            templateUrl: 'static/templates/system-list.html',
            controller: SystemListCtrl
          })
          .when('/:systemSlug', {
            templateUrl: 'static/templates/system-detail.html',
            controller: SystemDetailCtrl
          })
          .otherwise({
            redirectTo: '/'
          });
  });
