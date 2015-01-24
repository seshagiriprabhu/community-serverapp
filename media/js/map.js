/* Define base layers */
var cycleURL='http://{s}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png';
var cycleAttrib='Map data © OpenStreetMap contributors';
var opencyclemap = new L.TileLayer(cycleURL, {attribution: cycleAttrib}); 

var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © openstreetmap contributors';
var osm = new L.TileLayer(osmUrl, {attribution: osmAttrib}); 

var layer_geofences = new L.LayerGroup();
var array_geofences = new Array();
var markers = L.markerClusterGroup();
var popup = L.popup();

/* create custom marker which will represent locations in layer 'layer_apartments' */
customMarker = L.Marker.extend({
    options: { 
        title: 'User',
    }
});
function AddGeofenceToLayer() {
    for (var i=0; i<array_geofences.length; i++) {
        array_geofences[i].addTo(layer_geofences);
    }
}
/* Get all geofences from DB and add them to layer_geofences */
$.ajax({
    url: '/data_analysis/geofence/',
    type: 'GET',
    contentType: "application/json",
    dataType: "json",
    success: function(response) {
        $.each(eval(response), function(key, val) {      
            //fields in JSON that was returned          
            var fields = val.fields; 
            var lat = fields.latitude;
            var lon = fields.longitude;
            var rad = fields.geofence_radius;
            //function which creates and adds new markers based on filtered values
            var circle = L.circle(new L.LatLng(lat, lon), rad, {
                color: 'red',
                fillColor: '#f03',
                fillOpacity: 0.2,
                weight: 1,
                opacity: 0.3
            }); 
            circle.bindPopup("<strong>Geofence: </strong>" + fields.fence_name + 
                "<br><strong>Created by: </strong>" + fields.email); 
            circle.addTo(map);
            array_geofences.push(circle);
        });
        // add geofence to layer and add it to map
        AddGeofenceToLayer();
    }
});
/* Get all user updates from DB and add them to layer_locations */
$.ajax({
    url: '/data_analysis/location/',
    type: 'GET',
    contentType: "application/json",
    dataType: "json",
    success: function(response) {
        $.each(eval(response), function(key, val) {      
            //fields in JSON that was returned          
            var fields = val.fields; 
            var t_type = "Exited";
            // parse point field to get values of latitude and longitued
            var regExp = /\(([^)]+)\)/;
            var matches = regExp.exec(fields.geom);
            var point = matches[1];
            var lon=point.split(' ')[0];
            var lat=point.split(' ')[1];
            //function which creates and adds new markers based on filtered values
            marker = new customMarker([lat, lon], {
                title: fields.disp_name,
                opacity: 1.0  
            });
            if (fields.t_type == 1) {
                t_type = "Entered";
            }
            var date_time = new Date(fields.date_time);
            var hour = date_time.getHours();
            var mins = date_time.getMinutes();
            var date = date_time.getDate();
            var month = date_time.getUTCMonth();
            var year = date_time.getYear();
            var final_format = hour + ":" + mins + " " + date + "." + month + "." + year;
            marker.bindPopup("<strong>Name: </strong>" + fields.disp_name + 
                "<br><strong>Time: </strong>" + final_format + 
                "<br><strong>Transition Type: </strong>"+ t_type);
            markers.addLayer(marker);
        });
    }
});
/* create map object */
var map = L.map('map', {
    center: [51.54521, 9.93267],
    zoom: 14,
    fullscreenControl: true,
    fullscreenControlOptions: {
        position: 'topleft'
    },
    layers: [osm, markers, layer_geofences]
});

var baseLayers = {
    "OpenCycleMap": opencyclemap,
    "OpenStreetMap": osm
};

var overlays = {
    "Geofences": layer_geofences,
    "User location updates": markers
};

/* Zoom to bounds in one easy click */
markers.on('clusterclick', function (a) {
    a.layer.zoomToBounds();
});

markers.on('click', function (a) {
    console.log('marker ' + a.layer);
});

markers.on('clusterclick', function (a) {
    console.log('cluster ' + a.layer.getAllChildMarkers().length);
});
/* A function to return the LatLng of a place clicked on mapped */
function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}
map.on('click', onMapClick);
L.control.layers(baseLayers, overlays).addTo(map);

/* S I D E B A R   F I L T E R */
L.easyButton('fa-bars', 
           function() {sidebar.toggle();},
        ''
    )
var sidebar = L.control.sidebar('sidebar', {
    position: 'left'
});
map.addControl(sidebar);

$('#filter_control').click(function() {
    sidebar.show();
});

