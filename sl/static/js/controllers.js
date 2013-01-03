function SystemListCtrl($scope, $http, $resource){

    $scope.sl = $resource('stack/api/v1/system/search/',
        {format: 'json', q: ''});
    
    $scope.doSearch = function (){
        $scope.systems = $scope.sl.get({q:$scope.query});
    };

}

function SystemDetailCtrl($scope, $routeParams,  $http){
    $http.get('stack/api/v1/app/' + $routeParams.systemSlug + '/?format=json'
            ).success(function(system){
                $scope.system = system;
            });
}
