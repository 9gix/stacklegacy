function SystemListCtrl($scope, $http){
    $http.get('stack/api/v1/app/?format=json&limit=20').success(function(data){
        $scope.systems = data.objects;
    });
    $scope.orderProp = 'name';
}
