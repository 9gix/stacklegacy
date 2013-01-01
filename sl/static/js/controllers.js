function SystemListCtrl($scope, $http){
    $http.get('stack/api/v1/system/?format=json&limit=20&order_by=-modified_at').success(function(data){
        $scope.systems = data.objects;
    });
}

function SystemDetailCtrl($scope, $routeParams,  $http){
    $http.get('stack/api/v1/app/' + $routeParams.systemSlug + '/?format=json'
            ).success(function(system){
                $scope.system = system;
            });
}
