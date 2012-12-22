function SystemListCtrl($scope, $http){
    $http.get('stack/api/v1/app/?format=json&limit=2').success(function(data){
        $scope.systems = data.objects;
    });
    $scope.orderProp = 'name';
}

function SystemDetailCtrl($scope, $routeParams, $http){
    $http.get('stack/api/v1/app/' + $routeParams.systemId + '/?format=json'
            ).success(function(system){
                $scope.system = system;
            });
}
