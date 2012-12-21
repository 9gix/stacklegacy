'use strict';

var slApp = angular.module('slApp', [])
    .config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/systems', {
        templateUrl: 'static/templates/system-list.html',
        controller: SystemListCtrl
      })
      .when('/systems/:systemId', {
        templateUrl: 'static/templates/system-detail.html',
        controller: SystemDetailCtrl
      })
      .otherwise({
        redirectTo: '/systems'
      });
  }]);
