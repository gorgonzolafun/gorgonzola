$(function() {
    function init_map(mapID){
        var MapID = 'about-gmap-canvas';
        var MapContent = '<strong>Portami Via</strong><br>Bajo Izq., Carrer dels Ballesters, 3<br>46002 Valencia España<br>';

        var myOptions = {
            zoom: 15,
            center: new google.maps.LatLng(39.4711565, -0.37471030000006067),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        map = new google.maps.Map(document.getElementById(MapID), myOptions);
        marker = new google.maps.Marker({
            map: map,
            position: new google.maps.LatLng(39.4711565, -0.37471030000006067)
        });
        infowindow = new google.maps.InfoWindow({
            content: MapContent
        });
        google.maps.event.addListener(marker, 'click', function(){
            infowindow.open(map, marker);
        });
        // Open
        infowindow.open(map, marker);
    }
    google.maps.event.addDomListener(window, 'load', init_map);
});
