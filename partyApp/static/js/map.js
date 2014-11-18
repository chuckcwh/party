$(document).ready(function(){




    function initialize() {
//        if(!!navigator.geolocation) {
        var mapOptions = {
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        navigator.geolocation.getCurrentPosition(function(position) {
            geolocate = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
            var image = 'img/man_icon.png';
            myLat = position.coords.latitude;
            myLon = position.coords.longitude;
//            var infowindow = new google.maps.InfoWindow({
//                map: map,
//                position: geolocate,
//                content:
//                    '<h4>Your Location</h1>' +
//                    '<p>Latitude: ' + myLat + '</p>' +
//                    '<p>Longitude: ' + myLon + '</p>'
//            });
            map.setCenter(geolocate);

            var myImage = {
                url: '../static/img/man_icon2.png'
//                size: new google.maps.Size(20, 32),
//                origin: new google.maps.Point(0,0),
//                anchor: new google.maps.Point(0, 0)
            };
            var shape = {
                coords: [1, 1, 1, 20, 18, 20, 18 , 1],
                type: 'poly'
            };
            var myPlace = ['Here You Are!', myLat, myLon, 1];
            var myself = new google.maps.Marker({
                position: new google.maps.LatLng(myPlace[1], myPlace[2]),
                map: map,
                icon: myImage,
                shape: shape,
                title: myPlace[0],
                zIndex: myPlace[3]
            })

        });
//        } else {
//            document.getElementById('map_canvas').innerHTML = 'No Geolocation Support.';
//        }
        var map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);

    }
    google.maps.event.addDomListener(window, 'load', initialize);




    //    if (err.code == 0) {
    //        console.log('unknown error')
    //    }
    //    if (err.code == 1) {
    //        console.log('Access denied by user')
    //    }
    //    if (err.code == 2) {
    //        console.log('Position unavailable')
    //    }
    //    if (err.code == 3) {
    //        console.log('Timed out')
    //    }
});