function SystemListCtrl($scope, $location){

    
    $scope.doSearch = function (){
        if ($scope.query){
            $location.path('/search').search('q', $scope.query);
        }else{
            $location.path('/');
        }
    };

}

function HomeCtrl($scope, $http){
    $http.get('stack/api/v1/system/?format=json'
            ).success(function(result){
                $scope.systems = result;
            });
}

function UpdatedSystemListCtrl($scope, $http){
    $http.get('stack/api/v1/system/?format=json&order_by=-modified_at'
            ).success(function(result){
                $scope.systems = result;
            });
}

function LatestSystemListCtrl($scope, $http){
    $http.get('stack/api/v1/system/?format=json&order_by=-created_at'
            ).success(function(result){
                $scope.systems = result;
            });
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
