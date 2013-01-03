function SystemListCtrl($scope, $location){

    
    $scope.doSearch = function (){
        if ($scope.query){
            $location.path('/search').search('q', $scope.query);
        }else{
            $location.path('/');
        }
    };

}

function SystemSearchCtrl($scope, $resource, $routeParams){
    $scope.query = $routeParams.q;
    $scope.sl = $resource('stack/api/v1/system/search/', {format: 'json', q: ''});
    $scope.$on('$routeUpdate', function(){
        $scope.systems = $scope.sl.get({q:$routeParams.q});
    });
    $scope.$broadcast('$routeUpdate');
}
function SystemDetailCtrl($scope, $routeParams,  $http){
    $http.get('stack/api/v1/app/' + $routeParams.systemSlug + '/?format=json'
            ).success(function(system){
                $scope.system = system;
            });
}
