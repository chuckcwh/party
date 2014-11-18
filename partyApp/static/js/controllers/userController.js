function userController($scope, $http, $routeParams) {

    var userId = $routeParams.userId;

    $http.get('/api/profiles/' + userId).success(function(response){
        console.log(response);
        $scope.user = response;
    })
}