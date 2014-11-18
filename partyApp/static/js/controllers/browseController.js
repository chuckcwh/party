function browseController($scope, $filter, myLocation, partyLocation) {

    //party list
    $scope.parties = partyLocation.response.results;

    var createPartyMarker = function(i) {
        spot = {
            title: $scope.parties[i].title,
            id: $scope.parties[i].id,
            location: { latitude: $scope.parties[i].latitude,
                longitude: $scope.parties[i].longitude }
        };
        return spot
    };
    var addMarker = [];
    for (var i= 0; i<$scope.parties.length; i++) {
        addMarker.push(createPartyMarker(i))
    }
    $scope.partyMarker = addMarker;
    console.log($scope.partyMarker);

    $scope.$watch("partyKwd", function(partyKwd) {
        $scope.filterPartyMarker = $filter("filter")($scope.partyMarker, partyKwd);
        if (!$scope.filterPartyMarker){
        }
    });



    //map info
    $scope.map = {
        center: { latitude: myLocation['myLat'], longitude: myLocation['myLon'] },
        zoom: 14
    };
    $scope.circle = {
        center: { latitude: myLocation['myLat'], longitude: myLocation['myLon'] },
        radius: 1000,
        fill: { color: '#08B21F', opacity: 0.5 },
        stroke: {color: '#08B21F', weight: 1, opacity: 1}
    };
    $scope.marker = {
        id: 0,
        coords: { latitude: myLocation['myLat'], longitude: myLocation['myLon'] }
    };

}