function browseController($scope, $filter, myLocation, partyLocation) {

    //party list
    $scope.parties = partyLocation.response.results;
    console.log($scope.parties);

    var createPartyMarker = function(i) {
        spot = {
            title: $scope.parties[i].title,
            id: $scope.parties[i].id,
            location: { latitude: $scope.parties[i].latitude,
                longitude: $scope.parties[i].longitude },
            icon: "/static/img/party-icon.png"
        };
        return spot
    };
    var addMarker = [];
    for (var i= 0; i<$scope.parties.length; i++) {
        addMarker.push(createPartyMarker(i));
    }
    $scope.partyMarker = addMarker;
    console.log($scope.partyMarker);

    $scope.$watch("partyKwd", function(partyKwd) {
        $scope.filteredMarkers =  $filter("filter")($scope.partyMarker, partyKwd);
        angular.forEach(addMarker,function(marker){
            marker.showWindow = false;
            marker.onClick = function(){
                console.log('on click - opening window');
                marker.showWindow = true;
                $scope.$apply();
            };
            marker.closeClick = function() {
                console.log('close click - hiding window');
                marker.showWindow = false;
                $scope.$apply();
            };
        });
        $scope.filterPartyMarker = $scope.filteredMarkers;
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
        radius: 1500,
        fill: { color: '#08B21F', opacity: 0.5 },
        stroke: {color: '#08B21F', weight: 1, opacity: 1}
    };
    $scope.options = {scrollwheel: false};
    $scope.marker = {
        id: 0,
        coords: { latitude: myLocation['myLat'], longitude: myLocation['myLon'] },
        icon: "/static/img/Superman-icon.png"
    };




    $scope.check = true;
    $scope.toggleCard = function() {
        $scope.check = $scope.check === false ? true: false;
    };

}