function userController($scope, $http, $location,$routeParams, $rootScope) {

    var userId = $routeParams.userId;
    $rootScope.userId = userId;
    //show login user
    $http.get('/api/v1/profiles/' + userId).success(function(response){
        console.log(response);
        $scope.user = response;
    });

    //Add parties doesnt work
    $scope.addParty = function() {
        var getOwnerId;
        for (i = 0; i < $scope.userList.length; i++) {
            if (i.username === $scope.party.owner) {
                getOwnerId = i.username
            }
        }
        var data = {
            'owner': getOwnerId,
            'title': $scope.party.title,
            'latitude': $scope.party.latitude,
            'longitude': $scope.party.longitude,
            'time': $scope.party.time
        };
        
        // Would be good to put your API calls from your controllers into a service/factory
        $http.post('/api/v1/parties/', data)
            .success(function(response) {
                $scope.partyPageChanged();
                $scope.party = {};
            }).error(function(error){
                console.log(error);
            })
    };

}
